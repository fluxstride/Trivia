
from crypt import methods
from email import message
import os
from unicodedata import category
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category, db

QUESTIONS_PER_PAGE = 10


def paginate_questions(request, selection):
    page = request.args.get("page", 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [category.format() for category in selection]
    paginated_selection = questions[start:end]
    return paginated_selection


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.json.sort_keys = False
    setup_db(app)

    """
    @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
    """
    CORS(app, resources={"/": {"origins": "*"}})

    """
    @TODO: Use the after_request decorator to set Access-Control-Allow
    """
    @app.after_request
    def after_request(response):
        response.headers.add("Access-Control-Allow-Headers",
                             "Content-Type, Authorization")
        response.headers.add("Access-Control-Allow-Methods",
                             "GET,POST,PATCH,PUT,DELETE,OPTIONS")
        return response

    @app.route("/")
    def index():
        return jsonify({
            "success": True,
            "message": "Welcome to Trivia API"
        })

    """
    @TODO:
    Create an endpoint to handle GET requests
    for all available categories.
    """
    @app.route("/categories", methods=['GET'])
    def cartegories():
        selection = Category.query.order_by(Category.id).all()
        categories = {category.id: category.type
                      for category in selection}

        return jsonify({"success": True, "categories": categories, "total_categories": len(categories)})

    """
    @TODO:
    Create an endpoint to handle GET requests for questions,
    including pagination (every 10 questions).
    This endpoint should return a list of questions,
    number of total questions, current category, categories.

    TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination at the bottom of the screen for three pages.
    Clicking on the page numbers should update the questions.
    """

    @app.route("/questions", methods=["GET"])
    def get_questions():
        page = request.args.get("page", 1, type=int)
        all_categories = Category.query.order_by(Category.id).all()
        all_questions = Question.query.order_by(Question.id).all()
        categories = {category.id: category.type
                      for category in all_categories}
        questions = paginate_questions(
            request=request, selection=all_questions)

        return jsonify({
            "success": True,
            "questions": questions,
            "total_questions": len(all_questions),
            "categories": categories,
            "current_category": None,
            "page": page
        })

    """
    @TODO:
    Create an endpoint to DELETE question using a question ID.

    TEST: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page.
    """
    @app.route("/questions/<int:id>", methods=["DELETE"])
    def delete_question(id):
        question_to_delete = Question.query.filter(
            Question.id == id).one_or_none()

        all_questions = Question.query.order_by(Question.id).all()
        questions = paginate_questions(
            request=request, selection=all_questions)

        if question_to_delete is None:
            abort(404)

        question_to_delete.delete()

        return jsonify({
            "success": True,
            "deleted": question_to_delete.id,
            "questions": questions,
            "total_questions": len(all_questions),

        })

    @app.route("/questions", methods=["POST"])
    def create_question():
        body = request.get_json()
        question = body.get("question", None)
        answer = body.get(
            "answer", None)
        category = body.get(
            "category", None)
        difficulty = body.get("difficulty", None)
        search = body.get("searchTerm")

        """
        @TODO:
        Create a POST endpoint to get questions based on a search term.
        It should return any questions for whom the search term
        is a substring of the question.

        TEST: Search by any phrase. The questions list will update to include
        only question that include that string within their question.
        Try using the word "title" to start.
        """
        if (search):
            search_term = "%{}%".format(search)
            selection = Question.query.filter(
                Question.question.ilike(search_term))
            current_questions = paginate_questions(
                request=request, selection=selection)

            return jsonify({
                "success": True,
                "questions": current_questions,
                "total_questions": len(selection.all())
            })

        else:
            """
            @TODO:
            Create an endpoint to POST a new question,
            which will require the question and answer text,
            category, and difficulty score.

            TEST: When you submit a question on the "Add" tab,
            the form will clear and the question will appear at the end of the last page
            of the questions list in the "List" tab.
            """
            question = Question(question=question, answer=answer,
                                category=category, difficulty=difficulty)
            question.insert()
            selection = Question.query.order_by(Question.id).all()
            current_questions = paginate_questions(
                request=request, selection=selection)

            return jsonify({
                "success": True,
                "created_question": question.id,
                "questions": current_questions
            })

    """
    @TODO:
    Create a GET endpoint to get questions based on category.

    TEST: In the "List" tab / main screen, clicking on one of the
    categories in the left column will cause only questions of that
    category to be shown.
    """
    @app.route("/categories/<int:category_id>/questions", methods=["GET"])
    def get_questions_by_category(category_id):
        categories_count = Category.query.count()

        if category_id > categories_count:
            abort(404)

        current_category = Category.query.filter(
            Category.id == category_id).one_or_none()
        selection = Question.query.filter(
            Question.category == category_id).all()
        current_questions = paginate_questions(
            request=request, selection=selection)

        return jsonify({
            "success": True,
            "questions": current_questions,
            "total_questions": len(selection),
            "current_category": current_category.type

        })

    """
    @TODO:
    Create a POST endpoint to get questions to play the quiz.
    This endpoint should take category and previous question parameters
    and return a random questions within the given category,
    if provided, and that is not one of the previous questions.

    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not.
    """
    @app.route("/quizzes", methods=["POST"])
    def get_quizzes():
        request_body = request.get_json()
        previous_questions = request_body.get("previous_questions", None)
        quiz_category = request_body.get("quiz_category", None)

        if previous_questions is None and quiz_category is None:
            abort(400)

        if quiz_category["id"] == 0:
            questions = [question.format()
                         for question in Question.query.all()]
        else:
            questions = [question.format() for question in Question.query.filter(
                Question.category == quiz_category["id"])]

        question = random.choice(questions)

        while True:
            if question["id"] in previous_questions:
                question = random.choice(questions)
            else:
                break

        return jsonify({
            "success": True,
            "question": question
        })

    """
    @TODO:
    Create error handlers for all expected errors
    including 404 and 422.
    """

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "method not allowed"
        }), 405

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    return app

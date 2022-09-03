# **Trivia App**

Trivia app is a quiz app for testing your knowlege in various fieds like.

- Science
- Art
- Geography
- History
- Entertainment
- Sports etc.

#

#

## **Getting Started**

### **Install Dependencies and run**

Run the commands below to install all the required dependencies to successfully run the app

### **Backend**

```bash
cd backend
pip install -r requirements.txt
```

#### **Start up the project**

```bash
export FLASK_APP=flaskr
export FLASK_DEBUG=true
flask run
```

**Base URL:**

#### `http://localhost:5000`

#

### **Frontend**

```bash
cd frontend
npm install
```

#### **Start up the project**

```bash
npm start
```

**Base URL:**

#### `http://localhost:3000`

#

## **Error Handling**

The API will return a **JSON** response with the format below it the request fails

```json
{
  "success": False,
  "error": 400,
  "message": "bad request"
}
```

#### API error types

- 400: Bad Request
- 404: resource not found
- 405: Method not allowed
- 422: Unprocessable request

#

#

## **Resources**

`GET "/"`

- Index route
- Request Arguments: None
- Sample request: `curl -X GET http://localhost:5000`

#### Response:

```json
{
  "success": true,
  "message": "Welcome to Trivia API"
}
```

#

`GET "/categories"`

- Returns a list of all categories of questions
- Request Arguments: None
- Sample request: `curl -X GET http://localhost:5000/categories`

#### Response:

```json
{
  "success": true,
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "total_categories": 6
}
```

#

`POST "/categories"`

- Creates a new category of question
- Request Arguments: None
- Sample request: `curl -X POST -H 'Content-Type:application/json' http://localhost:5000/categories -d '{"category":"tester"}'`

#### Request body sample

```json
{
  "category": "tester"
}
```

#### Response:

```json
{
  "success": true,
  "created_category": 13
}
```

#

`GET "/questions"`

- Returns a paginated list of questions
- Request Arguments: None
- Sample request: `curl -X GET http://localhost:5000/questions`

#### Response:

```json
{
  "success": true,
  "questions": [
    {
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?",
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4
    },
    {
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?",
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4
    },
    {
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?",
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2
    }
  ],
  "total_questions": 19,
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "current_category": null,
  "page": 1
}
```

#

`DELETE "/questions/<int:id>"`

- Deletes the question with given id if it exits in the database.
- Request Arguments: None
- Sample request: `curl -X DELETE http://localhost:5000/questions/5`

#### Response:

```json
{
  "success": true,
  "deleted": 5,
  "questions": [
    {
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?",
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4
    },
    {
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?",
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4
    },
    {
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?",
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2
    },
    {
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?",
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3
    }
  ],
  "total_questions": 19
}
```

#

`POST "/questions"`

- Used for:

  - Searching for a question in the database
  - Request Arguments: None
  - Sample request: `curl -X POST localhost:5000/questions -H 'Content-Type:application/json' -d '{ "searchTerm": "original" }' `

    #### Request body sample:

    ```json
    {
      "searchTerm": "original"
    }
    ```

    #### Response:

    ```json
    {
      "success": true,
      "questions": [
        {
          "id": 9,
          "question": "What boxer's original name is Cassius Clay?",
          "answer": "Muhammad Ali",
          "category": 4,
          "difficulty": 1
        }
      ],
      "total_questions": 1
    }
    ```

    #

  - Creating a new question under a specified category
  - Request Arguments: None
  - Sample request: `curl -X POST localhost:5000/questions -H 'Content-Type:application/json' -d '{"question": "What is the name of the highest mountain?","answer":"Mount Everest","category": 3,"difficulty": 1}' `

    #### Request body sample:

    ```json
    {
      "question": "What is the name of the highest mountain?",
      "answer": "Mount Everest",
      "category": 3,
      "difficulty": 1
    }
    ```

    #### Response sample:

    ```json
    {
      "success": true,
      "created_question": 26,
      "questions": [
        {
          "id": 2,
          "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?",
          "answer": "Apollo 13",
          "category": 5,
          "difficulty": 4
        },
        {
          "id": 4,
          "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?",
          "answer": "Tom Cruise",
          "category": 5,
          "difficulty": 4
        },
        {
          "id": 6,
          "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?",
          "answer": "Edward Scissorhands",
          "category": 5,
          "difficulty": 3
        },
        {
          "id": 9,
          "question": "What boxer's original name is Cassius Clay?",
          "answer": "Muhammad Ali",
          "category": 4,
          "difficulty": 1
        },
        {
          "id": 10,
          "question": "Which is the only team to play in every soccer World Cup tournament?",
          "answer": "Brazil",
          "category": 6,
          "difficulty": 3
        },
        {
          "id": 11,
          "question": "Which country won the first ever soccer World Cup in 1930?",
          "answer": "Uruguay",
          "category": 6,
          "difficulty": 4
        },
        {
          "id": 12,
          "question": "Who invented Peanut Butter?",
          "answer": "George Washington Carver",
          "category": 4,
          "difficulty": 2
        },
        {
          "id": 13,
          "question": "What is the largest lake in Africa?",
          "answer": "Lake Victoria",
          "category": 3,
          "difficulty": 2
        },
        {
          "id": 14,
          "question": "In which royal palace would you find the Hall of Mirrors?",
          "answer": "The Palace of Versailles",
          "category": 3,
          "difficulty": 3
        },
        {
          "id": 15,
          "question": "The Taj Mahal is located in which Indian city?",
          "answer": "Agra",
          "category": 3,
          "difficulty": 2
        }
      ]
    }
    ```

`GET "/categories/<int:category_id>/questions"`

- Return a list of questions under the category with the specified **`category_id`**
  - All category IDs
    - 1 - Science
    - 2 - Art
    - 3 - Geography
    - 4 - History
    - 5 - Entertainment
    - 6 - Sports
- Request Arguments: None
- Sample request: `curl -X GET http://localhost:5000/categories/1/questions`

#### Response

```json
{
  "questions": [
    {
      "id": 20,
      "question": "What is the heaviest organ in the human body?",
      "answer": "The Liver",
      "category": 1,
      "difficulty": 4
    },
    {
      "id": 21,
      "question": "Who discovered penicillin?",
      "answer": "Alexander Fleming",
      "category": 1,
      "difficulty": 3
    },
    {
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?",
      "answer": "Blood",
      "category": 1,
      "difficulty": 4
    }
  ],
  "total_questions": 3,
  "current_category": "Science"
}
```

`POST "/quizzes"`

- Return random questions based on the specified question category
- Request Arguments: None
- Sample request: `curl -X POST -H 'Content-Type:application/json' http://localhost:5000/quizzes -d '{ "previous_questions": [], "quiz_category": { "type": "Science", "id": 1 } }'`

#### Request body sample

```json
{
  "previous_questions": [],
  "quiz_category": { "type": "Science", "id": 1 }
}
```

#### Response

```json
{
  "success": true,
  "question": {
    "id": 21,
    "question": "Who discovered penicillin?",
    "answer": "Alexander Fleming",
    "category": 1,
    "difficulty": 3
  }
}
```

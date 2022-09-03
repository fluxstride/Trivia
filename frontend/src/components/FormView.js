import React, { Component } from "react";
import $ from "jquery";
import "../stylesheets/FormView.css";

class FormView extends Component {
  constructor(props) {
    super();
    this.state = {
      question: {
        question: "",
        answer: "",
        difficulty: 1,
        category: 1,
        rating: 1,
        categories: {},
      },
      category: "",
    };
  }

  componentDidMount() {
    $.ajax({
      url: `/categories`, //TODO: update request URL
      type: "GET",
      success: (result) => {
        this.setState({
          ...this.state,
          question: { ...this.state.question, categories: result.categories },
        });
        return;
      },
      error: (error) => {
        alert("Unable to load categories. Please try your request again");
        return;
      },
    });
  }

  submitQuestion = (event) => {
    event.preventDefault();
    $.ajax({
      url: "/questions", //TODO: update request URL
      type: "POST",
      dataType: "json",
      contentType: "application/json",
      data: JSON.stringify({
        question: this.state.question.question,
        answer: this.state.question.answer,
        difficulty: this.state.question.difficulty,
        category: this.state.question.category,
        rating: this.state.question.rating,
      }),
      xhrFields: {
        withCredentials: true,
      },
      crossDomain: true,
      success: (result) => {
        document.getElementById("add-question-form").reset();
        window.location.href = window.location.origin;
        return;
      },
      error: (error) => {
        alert("Unable to add question. Please try your request again");
        return;
      },
    });
  };
  submitCategory = (event) => {
    event.preventDefault();
    $.ajax({
      url: "/categories", //TODO: update request URL
      type: "POST",
      dataType: "json",
      contentType: "application/json",
      data: JSON.stringify({
        category: this.state.category,
      }),
      xhrFields: {
        withCredentials: true,
      },
      crossDomain: true,
      success: (result) => {
        document.getElementById("add-category-form").reset();
        window.location.href = window.location.origin;

        return;
      },
      error: (error) => {
        alert("Unable to add category. Please try your request again");
        return;
      },
    });
  };

  handleQuestionFormChange = ({ target: { name, value } }) => {
    this.setState({
      ...this.state,
      question: { ...this.state.question, [name]: value },
    });
  };

  handleCategoryFormChange = ({ target: { value } }) => {
    this.setState({
      ...this.state,
      category: value,
    });
  };

  render() {
    return (
      <div id="add-form">
        <h2>Add a New Trivia Question</h2>
        <form
          className="form-view"
          id="add-question-form"
          onSubmit={this.submitQuestion}
        >
          <label>
            Question
            <input
              type="text"
              name="question"
              onChange={this.handleQuestionFormChange}
            />
          </label>
          <label>
            Answer
            <input
              type="text"
              name="answer"
              onChange={this.handleQuestionFormChange}
            />
          </label>
          <label>
            Difficulty
            <select name="difficulty" onChange={this.handleQuestionFormChange}>
              <option value="1">1</option>
              <option value="2">2</option>
              <option value="3">3</option>
              <option value="4">4</option>
              <option value="5">5</option>
            </select>
          </label>
          <label>
            Rating
            <select name="rating" onChange={this.handleQuestionFormChange}>
              <option value="1">1</option>
              <option value="2">2</option>
              <option value="3">3</option>
              <option value="4">4</option>
              <option value="5">5</option>
            </select>
          </label>
          <label>
            Category
            <select name="category" onChange={this.handleQuestionFormChange}>
              {Object.keys(this.state.question.categories).map((id) => {
                return (
                  <option key={id} value={id}>
                    {this.state.question.categories[id]}
                  </option>
                );
              })}
            </select>
          </label>
          <input type="submit" className="button" value="Submit" />
        </form>

        {/* Add a new category */}
        <h2>Add a New Category</h2>
        <form
          className="form-view"
          id="add-category-form"
          onSubmit={this.submitCategory}
        >
          <label>
            Category
            <input
              type="text"
              name="question"
              onChange={this.handleCategoryFormChange}
            />
          </label>
          <input type="submit" className="button" value="Submit" />
        </form>
      </div>
    );
  }
}

export default FormView;

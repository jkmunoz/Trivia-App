import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from . models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10   

def paginate_questions(request, selection):
    # Use arguments to get the page number.
    page = request.args.get('page', 1, type=int)
    start = (page -1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    # Use list interpolation to format lists of questions appropriately
    # and return specific lists of questions. 
    questions = [question.format() for question in selection]
    current_questions = questions[start:end]

    return current_questions

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.app_context().push()
    setup_db(app)
    CORS(app)

    """
    DONE? Allowing '*' is automatic and I don't see a sample route.
     @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
    """
    
    """
    DONE @TODO: Use the after_request decorator to set Access-Control-Allow
    """
    # CORS headers
    @app.after_request
    def after_request(response):
        response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization,true")
        response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS")
        return response


    """
    DONE @TODO:
    Create an endpoint to handle GET requests
    for all available categories.
    """
# Retrieves all categories then formats them as a dictionary; the key being the ID and category types being the values.
    @app.route('/categories')
    def retrieves_categories():
        categories = Category.query.all()
        formatted_categories = {category.id: category.type for category in categories}

        return jsonify({
            'success': True,
            'categories': formatted_categories,
        })

    """
    DONE @TODO:
    Create an endpoint to handle GET requests for questions,
    including pagination (every 10 questions).
    This endpoint should return a list of questions,
    number of total questions, current category, categories.

    TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination at the bottom of the screen for three pages.
    Clicking on the page numbers should update the questions.
    """
# Retrieves paginated questions based on the chosen category IF one if chosen (10/ page), otherwise all Q's are returned. 
# Returns a list of questions, a number of total Q's, the current category, and all categories. 
    @app.route('/questions')
    def retrieves_questions():
        category = request.args.get('category', None)
        if category:
            selection = Question.query.filter_by(Question.category).all()
        else:
            selection = Question.query.order_by(Question.category).all()
        formatted_questions = paginate_questions(request, selection)
        categories = Category.query.all()
        formatted_categories = {category.id: category.type for category in categories}


        if len(formatted_questions) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'questions': formatted_questions,
            'total_questions': len(Question.query.all()),
            'current_category': category,
            'all_categories': formatted_categories,
        })

    """
    @TODO:
    Create an endpoint to DELETE question using a question ID.

    TEST: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page.
    """

    """
    @TODO:
    Create an endpoint to POST a new question,
    which will require the question and answer text,
    category, and difficulty score.

    TEST: When you submit a question on the "Add" tab,
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.
    """

    """
    @TODO:
    Create a POST endpoint to get questions based on a search term.
    It should return any questions for whom the search term
    is a substring of the question.

    TEST: Search by any phrase. The questions list will update to include
    only question that include that string within their question.
    Try using the word "title" to start.
    """

    """
    @TODO:
    Create a GET endpoint to get questions based on category.

    TEST: In the "List" tab / main screen, clicking on one of the
    categories in the left column will cause only questions of that
    category to be shown.
    """

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

    """
    @TODO:
    Create error handlers for all expected errors
    including 404 and 422.
    """

    return app


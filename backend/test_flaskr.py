import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgresql://{}:{}@{}/{}".format('postgres', 'postgres', 'localhost:5432', self.database_name)
        self.new_question = {'question': 'What is the Texas state capital?', 'answer': 'Austin', 'category': '3', 'difficulty': '1'}
        # setup_db(self.app, self.database_path)

    #    # binds the app to the current context
    #     with self.app.app_context():
    #         self.db = SQLAlchemy()
    #         self.db.init_app(self.app)
    #         # create all tables
    #         self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """   
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    # # Test 1.a for success getting questions.
    # def test_get_paginated_questions(self):
    #     res = self.client().get('/questions/')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['total_questions'])
    #     self.assertTrue(len(data['questions']))

    # # Test 1.b for failure getting questions.
    # def test_404_requesting_beyond_valid_page(self):
    #     res = self.client().get('/questions/?page=1000', json={'category': 'art'})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'Not found')

    # # Test 2.a for success getting all categories.
    # def test_get_categories(self):
    #     res = self.client().get('/categories/')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['categories'])
    #     self.assertTrue(len(data['categories']))

    # # Test 2.b for failure getting list of categories.
    # def test_404_if_no_categories_exist(self):
    #     res = self.client().get('/categories/') 
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 500)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['message'], 'Internal Server Error')

    # # Test 3.a for success deleting a question.
    # def test_delete_question(self):
    #     res = self.client().delete('/questions/5/')
    #     data = json.loads(res.data)

    #     question = Question.query.filter(Question.id == 5).one_or_none()

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['deleted'], 5)
    #     self.assertTrue(data['total_questions'])
    #     self.assertTrue(len(data['questions']))
    #     self.assertEqual(question, None)

    # # Test 3.b for failure deleting a question.
    # def test_422_if_question_does_not_exist(self):
    #     res = self.client().delete('/questions/1000/')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 422)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'Unprocessable')

    # # Test 4.a success posting a question.
    # def test_post_question(self):
    #     res  = self.client().post('/questions/', json=self.new_question)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['added'])
    #     self.assertTrue(len(data['questions']))

    # # Test 4.b failure to post a question.
    # def test_404_creation_not_allowed(self):
    #     res = self.client().post('/questions/1000', json=self.new_question)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'Not found')

    # # Test 5.a success getting questions based on search terms.
    # def test_search_for_questions(self):
    #     search = {'searchTerm': 'What is',}
    #     res = self.client().post('/questions/', json=search)
    #     data = json.loads(res.data)
    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(len(data['questions']), 10)

    # # Test 5.b failure getting questions based on search terms.
    # # status code 200 is returned. Perhaps I didn't implement the search function properly?
    # def test_404_search_not_found(self):
    #     search = {'searchTerm': 'bleep bloop blop', }
    #     res = self.client().post('/questions/', json=search)
    #     data = json.loads(res.data)
    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'Not found')

    # # Test 6.a success getting questions based on category.
    # def test_questions_by_category(self):
    #     res = self.client().post('/questions/?category=2')
    #     data = json.loads(res.data)
    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertNotEqual(len(data['questions']), 0)
    #     self.assertEqual(data['current_category'], '2')

    # # Test 6.b failure getting questions based on category.
    # def test_404_questions_by_category_not_found(self):
    #     res = self.client().get('/questions/?category=100')
    #     data = json.loads(res.data)
    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'Not found')

    # Test 7.a success getting questions to play the quiz.
    def test_questions_to_play_quiz(self):
        quiz = { 'previous_questions': [9],
                'category': {
                    'type': 'History',
                    'id': '4'
                }}
        res = self.client().post('/quizzes/', json=quiz)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    # Test 7.b failure getting questions to play the quiz.
    def test_422_questions_to_play_not_found(self):
        quiz = { 'previous_questions': [10000],
                'category': {
                    'type': 'bloop',
                    'id': 'blah'
                }}
        res = self.client().post('/quizzes/', json=quiz)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        # self.assertEqual(data['message'], 'Unprocessable')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
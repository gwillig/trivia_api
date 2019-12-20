import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from backend.flaskr import create_app
from backend.models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    @classmethod
    def setUpClass(cls):
        """Define test variables and initialize app."""

        cls.app = create_app()
        cls.client = cls.app.test_client

        cls.database_path = 'postgresql://test:test@localhost:15432/trivia_test'
        cls.db = setup_db(cls.app, cls.database_path)

        # binds the app to the current context
        with cls.app.app_context():
            cls.db = SQLAlchemy()
            cls.db.init_app(cls.app)
            # create all tables
            cls.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_questions(self):
        response = self.client().get('/questions')
        response_data = json.loads(response.data)
        ## Check response
        self.assertEqual(response.status_code,200)
        self.assertEqual(response_data['success'], True)

    def test_post_question_create_new_question(self):
        self.db = setup_db(self.app, self.database_path)
        '#1.Step: Create a new question'
        new_question = {'answer': 'Green',
                         'category': 1,
                         'difficulty': 2,
                         'question': "Which color has grass?"}
        '#2.Step: Send new question to database'
        response = self.client().post('/questions', data=json.dumps(new_question))
        '#3.Step: Check check the response code'
        self.assertEqual(response.status_code,200)
        '#3.Step: Delete the new question from the database'
        self.db.session.query(Question).filter_by(question="Which color has grass?").delete()

    def test_delete_question(self):

        self.db = setup_db(self.app, self.database_path)
        new_question = {'answer': 'Green',
                         'category': 1,
                         'difficulty': 2,
                         'question': "Which color has grass?"}
        '#2.Step: Send new question to database'
        q1=Question(**new_question)
        self.db.session.add(q1)
        self.db.session.commit()
        question_id = self.db.session.query(Question).filter_by(question="Which color has grass?").first().id
        '#2.Step: Send new question to database'
        response = self.client().delete(f'/questions/{question_id}')
        '#3.Step: Check check the response code'
        self.assertEqual(response.status_code,200)

    def test_get_categories(self):
        '#1.Step. Request categories'
        response = self.client().get('/categories/')
        '#2.Step: Check check the response code'
        self.assertEqual(response.status_code,200)

    def test_get_all_question_category(self):
        self.db = setup_db(self.app, self.database_path)
        category_id = self.db.session.query(Question).first().category
        response = self.client().get(f'/categories/{category_id}/questions')
        '#2.Step: Check check the response code'
        self.assertEqual(response.status_code,200)

    def test_get_quiz_questions(self):
        response = self.client().post('/quizzes',data=json.dumps({"previous_questions":[],"quiz_category":{'id':1}}))
        '#2.Step: Check check the response code'
        self.assertEqual(response.status_code, 200)
    # Make the tests conveniently executable
if __name__ == "__main__":
   unittest.main()


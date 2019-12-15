# ----------------------------------------------------------------------------#
# Own Notes.
"""
Description                         | Cmd
to login as the right user for psql | PGUSER=test PGPASSWORD=test psql -h localhost trivia
Give all right to role              | GRANT ALL PRIVILEGES ON database test to test;
adds temporary git\bit to path      | "c:\Program Files\Git\bin\sh.exe" --login

PGUSER=test PGPASSWORD=test psql -h localhost todoapp
"""
# ----------------------------------------------------------------------------#
import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
import json

from backend.models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)

    db = setup_db(app)
    '1.Step: config cors'
    CORS(app)
    cors = CORS(app, resources={r"/*": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        '''
        Define access controll
        '''
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,POST,PUT,PATCH,DELETE,OPTIONS')
        return response

    @app.route("/questions")
    def get_questions():
        start_page = request.args.get('page', 1, type=int)
        end_page = start_page + QUESTIONS_PER_PAGE
        print("#"*15)
        print(start_page)
        print("#" * 15)

        try:
            all_questions = db.session.query(Question).order_by(Question.id).offset(start_page).limit(QUESTIONS_PER_PAGE).all()
            all_questions_list = [el.format() for el in all_questions]
            total_questions =  db.session.query(Question).order_by(Question.id).count()
            ## Get all categories
            all_categories_dict ={}
            all_categories = db.session.query(Category).all()
            for el in all_categories:
                all_categories_dict[el.id] = el.type
        except:
            db.session.rollback()
            abort(400)
        finally:
            db.session.close()
        return jsonify(
            {'success': True,
            'questions': all_questions_list,
            'categories': all_categories_dict,
            'total_questions':total_questions
             }

        )

    @app.route('/questions',methods=['POST'])
    def post_question():
        '''
        @description:
            adds a new question to the database
        '''
        '#1.Step: Get all parameters for the ajax request'
        # question = request.args.post('question', None, type=str)
        # answer = request.args.post('answer', None, type=str)
        # difficulty = request.args.post('difficulty',None,type=int)
        # category = request.args.post('category', None, type=str)
        data_string = request.data
        request_dict = json.loads(data_string)
        request_dict['id'] = None #Will be automaticlly created

        '#2.Step: create a new records a the database and send response back'
        try:
            c1 = Question(**request_dict)
            db.session.add(c1)
            db.session.commit()
            print("New question has been created")
            print(request_dict)
        except:
            db.session.rollback()
            db.session.close()
            print('An error occur during creating of')
            print(request_dict)
            abort(400)
        finally:
            db.session.close()
        return jsonify({
            'success': True,
        })

    @app.route("/categories/")
    def get_categories():
        '''
        @description:
            gets all question for a give category
        @return:
            all question for a given category
        '''
        '#1.Step: get the category id'
        category_id = request.args.get('')
        try:
            categories_tuple = db.session.query(Category.id,Category.type).all()
            categories_dict = {key:value for key,value in categories_tuple}
        except:
            db.session.rollback()
            db.session.close()
            abort(404)
        finally:
            db.session.close()

        return jsonify(
            {
                'success':True,
                'categories': categories_dict
            }
        )

    '''
  @TODO: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''

    '''
  @TODO: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''


    '''
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''

    '''
  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''

    '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''


    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success':False,
            "error":400,
            'message':'bad request'
        })

    @app.errorhandler(404)
    def resource_not_found(error):
        return jsonify({
            'success':False,
            'error':404,
            'message':'resource not found'
        })

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'success':False,
            'error':422,
            'message':'The server understands the content type of the request entity'
        })

    return app
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)


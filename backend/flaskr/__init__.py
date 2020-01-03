import os
from flask import Flask, request, abort, jsonify
from flask_cors import CORS
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
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,POST,PUT,PATCH,DELETE,OPTIONS')
        return response

    @app.route("/questions")
    def get_questions():
        start_page_raw = request.args.get('page', 1, type=int)
        start_page = (start_page_raw - 1) * 10
        try:
            all_questions = db.session.query(Question)\
                .order_by(Question.id)\
                .offset(start_page).limit(QUESTIONS_PER_PAGE).all()
            all_questions_list = [el.format() for el in all_questions]
            total_questions = db.session.query(Question)\
                .order_by(Question.id).count()
            # Get all categories
            all_categories_dict = {}
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
             'total_questions': total_questions
             }

        )

    @app.route('/questions', methods=['POST'])
    def post_question():
        """
        @description:
            adds a new question to the database or search for a question
        """
        '#1.Step: Get all parameters for the ajax request'
        data_string = request.data
        request_dict = json.loads(data_string)
        '#2.Step: create a new records a the database and send response back'

        if 'searchTerm' not in request_dict.keys():
            try:
                c1 = Question(**request_dict)
                db.session.add(c1)
                db.session.commit()
            except:
                db.session.rollback()
                db.session.close()
                print('An error occur during creating of question')
                print(request_dict)
                abort(422)
            finally:
                db.session.close()
            return jsonify({
                'success': True,
            })
        else:
            '# Get all categories'
            all_categories_dict = {}
            all_categories = db.session.query(Category).all()
            for el in all_categories:
                all_categories_dict[el.id] = el.type

            search_term = request_dict['searchTerm']
            print(search_term)
            baseQuery = db.session.query(Question).\
                filter(Question.question.like(f'%{search_term}%'))
            result = baseQuery.all()
            all_questions_list = [el.format() for el in result]
            total_questions = baseQuery.count()

            if total_questions == 0:
                all_questions_list = [{'answer': 'Maya Angelou',
                                       'category': '4',
                                       'difficulty': 2,
                                       'id': 1,
                                       'question': "No hits."
                                                   " Please change search term"
                                       }]

            return jsonify({
                'success': True,
                'categories': all_categories_dict,
                'questions': all_questions_list,
                'total_questions': total_questions
            })

    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
        """
        @description:
            deletes a given question from the database
        """

        '#1.Step: Get all parameters for the ajax request'
        print(question_id)
        try:
            db.session.query(Question).filter_by(id=question_id).delete()
            db.session.commit()
        except:
            db.session.rollback()
            db.session.close()
            abort(400)
        finally:
            db.session.close()

        return jsonify({
            'success': True
        })

    @app.route("/categories/")
    def get_categories():
        """
        @description:
            gets all question for a give category
        @return:
            all question for a given category
        """

        '#1.Step: get the category id'

        try:
            categories_tuple = db.session.query(Category.id, Category.type)\
                .all()
            categories_dict = {key: value for key, value in categories_tuple}
            db.session.close()
            return jsonify(
                {"success": True, "categories": categories_dict}
            )
        except:
            db.session.rollback()
            db.session.close()
            abort(404)

    @app.route('/categories/<int:category_id>/questions')
    def get_all_question_category(category_id):
        print(category_id)
        try:
            category_type = Category.query\
                .filter_by(id=category_id).first().format()
            all_questions = db.session.query(Question)\
                .filter_by(category=str(category_id)).all()
            all_questions_list = [el.format() for el in all_questions]
            total_questions = db.session.query(Question)\
                .order_by(Question.id).count()
            # Get all categories
            all_categories_dict = {}
            all_categories = db.session.query(Category).all()
            for el in all_categories:
                all_categories_dict[el.id] = el.type
        except:
            db.session.rollback()
            abort(404)
        finally:
            db.session.close()
        return jsonify(
            {'success': True,
             'questions': all_questions_list,
             'categories': all_categories_dict,
             'total_questions': total_questions,
             'current_category': category_type
             }

        )

    @app.route('/quizzes', methods=['POST'])
    def get_quiz_questions():
        """
        @description:
            get some random question
        """
        try:
            '#1.Step: Get all parametres from the request'
            data_string = request.data
            request_dict = json.loads(data_string)
            '#2.1.Step: All all question if all is selected'
            category_id = request_dict["quiz_category"]["id"]
            category_typ = db.session.query(Category)\
                .filter_by(id=category_id).first().type
            previous_questions = request_dict["previous_questions"]
            if category_id == 0:
                question = db.session.query(Question).first()
            else:
                basequey = db.session.query(Question).\
                    filter(Question.category == str(category_id))
                for question_id in previous_questions:
                    basequey = basequey.filter(Question.id != str(question_id))
                question = basequey.first()
                if basequey.count() == 0:
                    return jsonify(
                        dict(success=True,
                             question={"question": False, "success": True}
                             )
                    )
        except:
            db.session.rollback()
            abort(400)
        finally:
            db.session.close()
        return jsonify(dict(success=True, question=question.format()))

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify(dict(success=False, error=400,
                            message='bad request')), 400

    @app.errorhandler(404)
    def resource_not_found(error):
        return jsonify(dict(success=False, error=404,
                            message='resource not found')), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify(
            dict(success=False, error=422,
                 message='The server understands the '
                         'content type of the request entity')
        ), 422

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

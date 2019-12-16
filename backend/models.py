import os
from sqlalchemy import Column, String, Integer, create_engine

from flask_sqlalchemy import SQLAlchemy
import json


database_path = 'postgresql://test:test@localhost:15432/trivia'

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()
    return db

'''
Question

'''
class Question(db.Model):  
  __tablename__ = 'questions'

  id = Column(Integer, primary_key=True)
  question = Column(String)
  answer = Column(String)
  category = Column(String)
  difficulty = Column(Integer)

  def __init__(self, question, answer, category, difficulty):
    self.question = question
    self.answer = answer
    self.category = category
    self.difficulty = difficulty

  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'question': self.question,
      'answer': self.answer,
      'category': self.category,
      'difficulty': self.difficulty
    }

'''
Category

'''
class Category(db.Model):  
  __tablename__ = 'categories'

  id = Column(Integer, primary_key=True)
  type = Column(String)

  def __init__(self, type):
    self.type = type

  def format(self):
    return {
      'id': self.id,
      'type': self.type
    }


def inject_data():
    question_list = [{'answer': 'Maya Angelou',
                      'category': 4,
                      'difficulty': 2,
                      'id': 5,
                      'question': "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"},
                     {'answer': 'Muhammad Ali',
                      'category': 4,
                      'difficulty': 1,
                      'id': 9,
                      'question': "What boxer's original name is Cassius Clay?"},
                     {'answer': 'Apollo 13',
                      'category': 5,
                      'difficulty': 4,
                      'id': 2,
                      'question': 'What movie earned Tom Hanks his third straight Oscar nomination, in 1996?'},
                     {'answer': 'Tom Cruise',
                      'category': 5,
                      'difficulty': 4,
                      'id': 4,
                      'question': 'What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?'},
                     {'answer': 'Edward Scissorhands',
                      'category': 5,
                      'difficulty': 3,
                      'id': 6,
                      'question': 'What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?'},
                     {'answer': 'Brazil',
                      'category': 6,
                      'difficulty': 3,
                      'id': 10,
                      'question': 'Which is the only team to play in every soccer World Cup tournament?'},
                     {'answer': 'Uruguay',
                      'category': 6,
                      'difficulty': 4,
                      'id': 11,
                      'question': 'Which country won the first ever soccer World Cup in 1930?'},
                     {'answer': 'George Washington Carver',
                      'category': 4,
                      'difficulty': 2,
                      'id': 12,
                      'question': 'Who invented Peanut Butter?'},
                     {'answer': 'Lake Victoria',
                      'category': 3,
                      'difficulty': 2,
                      'id': 13,
                      'question': 'What is the largest lake in Africa?'},
                     {'answer': 'The Palace of Versailles',
                      'category': 3,
                      'difficulty': 3,
                      'id': 14,
                      'question': 'In which royal palace would you find the Hall of Mirrors?'},
                     {'answer': 'Agra',
                      'category': 3,
                      'difficulty': 2,
                      'id': 15,
                      'question': 'The Taj Mahal is located in which Indian city?'},
                     {'answer': 'Escher',
                      'category': 2,
                      'difficulty': 1,
                      'id': 16,
                      'question': 'Which Dutch graphic artist–initials M C was a creator of optical illusions?'},
                     {'answer': 'Mona Lisa',
                      'category': 2,
                      'difficulty': 3,
                      'id': 17,
                      'question': 'La Giaconda is better known as what?'},
                     {'answer': 'One',
                      'category': 2,
                      'difficulty': 4,
                      'id': 18,
                      'question': 'How many paintings did Van Gogh sell in his lifetime?'},
                     {'answer': 'Jackson Pollock',
                      'category': 2,
                      'difficulty': 2,
                      'id': 19,
                      'question': 'Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?'},
                     {'answer': 'The Liver',
                      'category': 1,
                      'difficulty': 4,
                      'id': 20,
                      'question': 'What is the heaviest organ in the human body?'},
                     {'answer': 'Alexander Fleming',
                      'category': 1,
                      'difficulty': 3,
                      'id': 21,
                      'question': 'Who discovered penicillin?'},
                     {'answer': 'Blood',
                      'category': 1,
                      'difficulty': 4,
                      'id': 22,
                      'question': 'Hematology is a branch of medicine involving the study of what?'},
                     {'answer': 'Scarab',
                      'category': 4,
                      'difficulty': 4,
                      'id': 23,
                      'question': 'Which dung beetle was worshipped by the ancient Egyptians?'}
                     ]
    for el in question_list:
        el.pop('id')
    question_objects = [Question(**el) for el in question_list]
    db.session.add_all(question_objects)
    db.session.commit()
    data_category = [{'id': 1, 'type': 'Science'},
                     {'id': 2, 'type': 'Art'},
                     {'id': 3, 'type': 'Geography'},
                     {'id': 4, 'type': 'History'},
                     {'id': 5, 'type': 'Entertainment'},
                     {'id': 6, 'type': 'Sports'}]
    for el in data_category:
        el.pop('id')
    data_object = [Category(**el) for el in data_category]
    db.session.add_all(data_object)
    db.session.commit()




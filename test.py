# simple unit tests done for building the database of the project

import os
import unittest

from config import basedir
from sqlalchemy import func
from app import app, db
from app.models import User, Question, Option, Quiz

class TestCase(unittest.TestCase):
    # setting up the temporary test.db database
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        db.create_all()
    # tearing down of the database
    def tearDown(self):
        db.session.remove()
        db.drop_all()

    # simple test to assign User to u
    def test_avatar(self):
        u = User(username='john', email='john@example.com')

    # test to add user to a temporary database and query the user
    def test_make_user(self):
        u = User(username='john', email='john@example.com')
        db.session.add(u)
        db.session.commit()
        print( "\n"+"test_make_unique_nickname made a user with username: "+db.session.query(User).first().username+"\n")


    # test to for option, question and quiz table with queries
    def test_for_building_database1(self):
        option1 = Option(option_body = 'World of Warcraft')
        option2 = Option(option_body = 'Team Fortress 2')
        option3 = Option(option_body = 'Steam')
        option4 = Option(option_body = 'Dota 2')
        question1 = Question(question_body = 'which one is a moba game?')
        option1.question = question1
        option2.question = question1
        option4.correct = True
        option4.question = question1
        option3.question = question1
        user1 = User(username='john', email='john@example.com')
        quiz1 = Quiz(usersesh = user1)
        
        db.session.add(quiz1)
        db.session.add(question1)
        db.session.commit()

        for question in db.session.query(Question).all():
            for option in question.options:
                print("test_for_building_database1 option: " + option.option_body)
        

        print ("test_for_building_database1 quiz to user relationship (expected answer 1) user_id is: " + str(db.session.query(User).first().quiz[0].user_id))

    #A test to get the sum of a column with query
    def test_for_sum(self):
        u = User(username='test1', email='test1@example.com')
        u2 = User(username='test2', email='test2@example.com')
        
        db.session.add(u)
        db.session.add(u2)
        db.session.commit()

        print("test_for_sum of 2 user autogenerated ID (expected result is 3) result: " + str(db.session.query(func.sum(User.id)).scalar()))
    
    

if __name__ == '__main__':
    unittest.main()
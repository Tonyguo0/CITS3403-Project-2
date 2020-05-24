The database will require multiple tables to store information used by the website. These tables will be drawn on draw.io in 
the future and provided as graphs to view here.

##### Useful resource for when defining many-to-many relationships such as genre-game (a game can be in more than one genre), question-genre, question-attribute, attribute-game, etc.
https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/


Tables that will be needed:

#### The user structure.
User
- id = int            //primary key
- username = varchar
- password_hash = varchar
- quizes = (not in graph)  //relationship - db.relationship('Quiz', backref='users', lazy='dynamic')
- feedback            //relationship(1-to-many) - db.relationship('Feedback', backref='users', lazy='dynamic')

#### A Quiz completed by a user.
Quiz
- id = int            //primary key
- result = int        //for holding the result of the whole quiz
- questions           //relationship(1-to-many) - db.relationship('Questions', backref='quiz', lazy='dynamic')
- user_id = int       //foreign key to user

#### The question structure.
Question 
- id = int            //primary key
- question_body = varchar      //the body of the question 
- options             //relationship(1-to-many) - db.relationship('Options', backref='question', lazy='dynamic')
- quiz_id             //foreign key - db.Column(Integer, ForeignKey('quiz.id'))

#### the options for the question structure
Option
- id = int            //primary key
- option_body = varchar    //one body of the option
- correct = bool      //if the option is correct
- question_id         //foreign key - db.Column(Integer, ForeignKey('question.id'))

#### Feedback given by users, to be viewed by admins.
Feedback 
- id = int            //primary key
- feedback_msg = varchar
- user_id             //foreign key


#### Long answers for manual assessment.
Long_Answers 
- id = int            //primary key
- user_id = int       //foreign key to the  user who submitted 
- question_id = int   //foreign key to question
- answer = varchar    //input from user
- response = varchar  //the manual assessment 




#### getting the data from relationships note:
- To get the data from the corresponding relationships for 1 to many: 
- parent.query.join(child).filter(child.child_attribute)

#### how to add data corresponding to the foreign key
- u = User(username='susan', email='susan@example.com')
- p = Post(body='my first post!', author=u)


### the querys to add the test data:
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
user1 = User.query.get(4)
quiz1 = Quiz(usersesh = user1)
db.session.add(quiz1)
db.session.add(question1)
db.session.commit()



can use this to find the child's attributes for 1 to many:
>>> quiz1.questions[0].questions_body
### interating through the quizes
for quizes in Quiz.query.all()


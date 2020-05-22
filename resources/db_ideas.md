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



#### Relationships brain storm
- Genre 1 to 1 Quiz
- Quiz 1 to many questions
- Attribute 1 to 1 Questions

#### getting the data from relationships note:
- To get the data from the corresponding relationships for 1 to many: 
- parent.query.join(child).filter(child.child_attribute)

#### how to add data corresponding to the foreign key
- u = User(username='susan', email='susan@example.com')
- p = Post(body='my first post!', author=u)




#### Feedback given by users, to be viewed by admins.
Feedback 
- id = int            //primary key
- feedback_msg = varchar
- user_id             //foreign key






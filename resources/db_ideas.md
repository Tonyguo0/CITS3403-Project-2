The database will require multiple tables to store information used by the website. These tables will be drawn on draw.io in 
the future and provided as graphs to view here.

##### Useful resource for when defining many-to-many relationships such as genre-game (a game can be in more than one genre), question-genre, question-attribute, attribute-game, etc.
https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/


Tables that will be needed:

#### The user structure.
User
- id = int            //primary key
- username = varchar
- pw_hash = varchar
- admin = bool
- quizes = (not in graph)  //relationship - db.relationship('Quiz', backref='quiz-taker', lazy='dynamic')


#### The question structure.
Question 
- id = int            //primary key
- question = varchar
- options = []        //is list supported in SQLite?
- genres = not in graph? //relationship - db.relationship('Genre', backref='question', lazy='dynamic')
- attribute = not in graph   //relationship(1-to-1) - db.relationship('Attribute', uselist= False,backref='question')


#### Long answers for manual assessment.
Long_Answers 
- id = int            //primary key
- user_id = int       //foreign key to the user who submitted 
- question_id = int   //foreign key to question
- answer = varchar    //input from user
- response = varchar  //the manual assessment 
- 


#### Feedback given by users, to be viewed by admins.
Feedback 
- id = int            //primary key
- feedback_msg = varchar


#### A Quiz completed by a user.
Quiz
- id = int            //primary key
- user_id = int       //foreign key to user
- result = int        //value is a foreign key to a game id???
- Attribute           //relationship
- Genre               //relationship(1-to-1) - db.relationship('Genre', uselist= False, backref='quiz')


#### An attribute of a question or outcome that is used with others to match a user to a game. 
Attribute
- id = int            //primary key
- score(for every game) = int [] //again is list supported in SQLite?
- question_id = int       //foreign key - db.Column(Integer, ForeignKey('question.id'))

#### Genre that games and questions fall under.
Genre
- id = int
- genre_name = varchar
- quiz_id = int       //foreign key - db.Column(Integer, ForeignKey('quiz.id'))

#### Game Structure.
Game
- id = int
- game_name = varchar
- attributes         //relationship - db.relationship('Attribute', backref='game', lazy='dynamic')

#### Relationships brain storm
- Genre 1 to 1 Quiz
- Genre 1 to many Games
- Quiz 1 to many questions
- Games(score) many to many Questions
- Attribute 1 to 1 Questions









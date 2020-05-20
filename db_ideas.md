The database will require multiple tables to store information used by the website. These tables will be drawn on draw.io in 
the future and provided as graphs to view here.

##### Useful resource for when defining many-to-many relationships such as genre-game (a game can be in more than one genre), question-genre, question-attribute, attribute-game, etc.
https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/


Tables that will be needed:

#### The user structure.
User
- id = int            //primary key
- username = varchar
- pw hash = varchar
- admin = bool
- results = (not in graph)  //db.relationship('Result', backref='quiz-taker', lazy='dynamic')


#### The question structure.
Question 
- id = int            //primary key
- question = varchar
- options = []        //is list supported in SQLite?
- genres = not in graph? //db.relationship('Genre', backref='question', lazy='dynamic')
- attribute = not in graph   //db.relationship('Attribute', backref='question', lazy='dynamic')


#### Long answers for manual assessment.
Long answers 
- id = int            //primary key
- user_id = int       //foreign key to the user who submitted 
- question_id = int   //foreign key to question
- answer = varchar    //input from user
- response = varchar  //the manual assessment 
- 


#### Feedback given by users, to be viewed by admins.
Feedback 
- id = int            //primary key
- 


#### A Quiz completed by a user.
Quiz
- id = int            //primary key
- user_id = int       //foreign key to user
- result = int        //value is a foreign key to a game id
- Attribute


#### An attribute of a question or outcome that is used with others to match a user to a game. 
Attribute
- id = int            //primary key


#### Genre that games and questions fall under.
Genre
- id = int
- 

#### Game Structure.
Game
- id = int
- attributes = db.relationship('Attribute', backref='game', lazy='dynamic')








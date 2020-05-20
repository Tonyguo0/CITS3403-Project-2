The database will require multiple tables to store information used by the website. These tables will be drawn on draw.io in 
the future and provided as graphs to view here.

# useful resource for when defining many-to-many relationships such as genre-game (a game can be in more than one genre), question-genre, question-attribute, attribute-game, etc.
https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/


Tables that will be needed:

# the user structure
User
- id = int            //primary key
- username = varchar
- pw hash = varchar
- admin = bool
- results = (not in graph)  //db.relationship('Result', backref='quiz-taker', lazy='dynamic')


# the question structure
Question 
- id = int            //primary key
- question = varchar
- options = []        //is list supported in SQLite?
- genres = not in graph? //db.relationship('Genre', backref='question', lazy='dynamic')
- attribute = not in graph   //db.relationship('Attribute', backref='question', lazy='dynamic')


# long answers for manual assessment
Long answers 
- id = int            //primary key
- user_id = int       //foreign key to the user who submitted 
- question_id = int   //foreign key to question
- answer = varchar    //input from user
- response = varchar  //the manual assessment 
- 


# feedback given by users
Feedback 
- id = int            //primary key
- 


# results of a quiz for a user 
Result
- id = int            //primary key
- user_id = int       //foreign key to user
- result = int        //value is a foreign key to a game id
- Attribute


# an attribute of a question/outcome that is used with others to match a user to a game 
Attribute
- id = int            //primary key


# the genre that games and questions fall under
Genre
- id = int
- 

# the structure holding a game
Game
- id = int
- attributes = db.relationship('Attribute', backref='game', lazy='dynamic')








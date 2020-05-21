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
- roles               //relationship(1-to-1) - db.relationship('Role', secondary = 'user_roles')
- quizes = (not in graph)  //relationship - db.relationship('Quiz', backref='quiz-taker', lazy='dynamic')

#### Define the Role Structure
Role
- _tablename_ = 'role'
- id = int              //primary key
- name = varchar        //name of the role

#### Define the UserRoles association table
UserRoles
- _tablename_ = 'user_roles'
- id = int
- user_id              //foreign key
- role_id              //foreign key


#### Feedback given by users, to be viewed by admins.
Feedback 
- id = int            //primary key
- feedback_msg = varchar


#### A Quiz completed by a user.
Quiz
- id = int            //primary key
- questions           //relationship(1-to-many) - db.relationship('Questions', backref='quiz', lazy='dynamic')
- game_counter = int  //counter used for each game
- user_id = int       //foreign key to user
- result = int        //foreign key - db.Column(Integer, ForeignKey('game.id'))
- genre               //relationship(1-to-1) - db.relationship('Genre', uselist= False, backref='quiz')

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
- question_id         //foreign key - db.Column(Integer, ForeignKey('question.id'))
- attribute           //relationship(1-to-many) - db.relationship('Attribute', backref='options', lazy='dynamic')

#### An attribute of a question or outcome that is used with others to match a user to a game. 
Attribute
- id = int            //primary key
- score_variant = int //score variant based on each option for each game
- option_id = int     //foreign key - db.Column(Integer, ForeignKey('option.id'))
- game_id = int       //foreign key - db.Column(Integer, ForeignKey('option.id'))

#### Genre that games and questions fall under.
Genre
- id = int
- genre_name = varchar
- quiz_id = int       //foreign key - db.Column(Integer, ForeignKey('quiz.id'))

#### Game Structure.
Game
- id = int
- game_name = varchar
- game_score = int      //for the score of the game
- Result                //relationship(1 to 1) - db.relationship('Quiz', uselist= False, backref='game')
- attribute             //relationship(1 to 1) - db.relationship('Attribute', uselist= False, backref='game')
- scores_id             //foreign key - db.Column(Integer, ForeignKey('scores.id'))
- genre_id



#### Relationships brain storm
- Genre 1 to 1 Quiz
- Genre 1 to many Games
- Quiz 1 to many questions
- Games 1 to 1 Quiz
- Attribute 1 to 1 Questions

#### getting the data from relationships note:
- To get the data from the corresponding relationships for 1 to many: 
- parent.query.join(child).filter(child.child_attribute)

#### how to add data corresponding to the foreign key
- u = User(username='susan', email='susan@example.com')
- p = Post(body='my first post!', author=u)









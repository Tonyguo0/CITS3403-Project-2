The database will require multiple tables to store information used by the website. These tables will be drawn on draw.io in 
the future and provided as graphs to view here.

Tables that will be needed:

User
- id = int            //primary key
- username = varchar
- pw hash = varchar
- admin = bool

Question 
- id = int            //primary key
- question = varchar
- options = []        //is list supported in SQLite?
- genres = []         //the genres that the question will appear in (e.g. all, sport, role-play etc.)
- attribute = int     //this is the attribute score the question will affect (e.g. fantasy etc.) which is used to decide the game recommendation


Long answers 
- id = int
- user_id = int       //foreign key to the user who submitted 
- question_id = int   //foreign key to question
- answer = varchar    //input from user
- response = varchar  //the manual assessment 
- 



# CITS3403-Project-2
Game of Quizes

Collaborated work of Tony Guo and Aiden Lewington

A simple web application that tests users on gaming trivia.

### Page 1.1:
A login page 

### Page 1.2: 
An account registeration page

### Page 2: 
The Quiz page where a user is required to log in before playing. All questions, multiple choice and long answer are displayed here.

### Page 3: 
Account page, where a user's quiz attempts are shown as well as giving them the opportunity to provide feedback. The manually assessed long answers will also appear here once answered.

### Page 4: 
Admin (add questions, games, manually assess the long answer questions, add and delete users) 
optionally: feedback page


Throughout this project a backlog was used to follow agile methodologies and is available here: https://trello.com/b/LtrpGwPM/cits3401-project-2

To list all packages used into a file use:
#### pip freeze | grep -v "pkg-resources" > requirements.txt

(removing pkg-resources as it is a known bug with pip freeze caused by ubuntu clients)
        - https://stackoverflow.com/a/40167445

# Set Up

Install virtual environment by using:
#### python3 -m venv virtual-environment 

Then enter the virtual environment using:
#### source virtual-environment/bin/activate

And install the requirements listed in requirements.txt:
#### pip install -r requirements.txt  

Once all packages are installed, the flask app can be run using:
#### flask run


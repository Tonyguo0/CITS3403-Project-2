# CITS3403-Project-2
Game of Quizes

Collaborated work of Tony Guo and Aiden Lewington

A simple web application that will suggest what game is suited for the user based on a variety of questions

page 1.1: login page 

page 1.2: registeration page

page 2: Questions (genre selection; with subset of questions for the genre - multiple choice quiz, long answer questions e.g. user specifying types of game, long paragraph about what they think they'd like for manual assessment etc... in the future maybe?)

page 3: Results (what game they'd like -info for game), info about their answer (attribute showing how they got the game), in the future maybe percentage of people for the answer

page 4: Admin (add questions, games, manually assess the long answer questions, add and delete users) 
optionally: feedback page

Project backlog using Trello (will be public when released): https://trello.com/b/LtrpGwPM/cits3401-project-2


# Set Up
To list all packages used in a file use:
#### pip freeze | grep -v "pkg-resources" > requirements.txt

(removing pkg-resources as it is a known bug with pip freeze caused by ubuntu)
        - https://stackoverflow.com/a/40167445

install virtual environment by doing:
#### python3 -m venv virtual-environment 

then enter the virtual environment using:
#### source virtual-environment/bin/activate

and install the requirements:
#### pip install -r requirements.txt  

to grab all the required packages for running the flask web application in the virtual environment






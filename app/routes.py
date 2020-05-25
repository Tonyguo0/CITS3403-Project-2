# Server side consisting of view functions which processes each page based on GET or Post method

from flask import Flask, session, render_template, flash, redirect, url_for, request
from app import app, db
from datetime import timedelta
from flask_login import current_user, login_user, logout_user, login_required
from sqlalchemy import func
from app.models import User, Question, Option, Quiz, Long_Answers, Feedbacks
from app.forms import LoginForm, RegistrationForm
from werkzeug.urls import url_parse
from flask_user import roles_required

# log out user after every 5 mins of true inactivity
@app.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)
    # resets the time
    session.modified = True


@app.route('/')
@app.route('/general')
# a welcome page which displays the general statistics of the game 
def general():

    users = User.query.all()
    avg = 0
    numUser = 0
    shortqpercent = 0
    avglong = 0
    numUserlonganswer = 0
    # calculate the user's avg marks for short answer question
    for user in users:
        if not bool(user.quiz.first()):
            continue
        else:
            numUser +=1
            avg += user.quiz[0].result
        for longanswer in user.long_answer:
            if longanswer.mark != None:
                numUserlonganswer += 1
                avglong+= longanswer.mark
    # calculate the user's avg marks for long answer question
    longquestions =  Question.query.filter_by(long_question = True)
    numlongq =longquestions.count()
    if numlongq !=0:
        numUserlonganswer /= numlongq
        numUserlonganswer = int(numUserlonganswer)
        longqmark = 0
        for longquestion in longquestions:
            longqmark += longquestion.mark_for_question
        

    # getting the avg for the long answers
    if numUser!=0:
        avg = round(avg/numUser,2)
        avglong = round(avglong/numUserlonganswer,2)
    # getting the marks for the short answers
    if db.session.query(func.sum(Question.mark_for_question)).filter_by(long_question = False).scalar() != None:
        shortqmarks = db.session.query(func.sum(Question.mark_for_question)).filter_by(long_question = False).scalar()
    # getting percentage for both
    if shortqmarks!=0:
        shortqpercent = round((avg/shortqmarks)*100, 2)
    if numlongq !=0:
        longqpercent = round((avglong/longqmark)*100,2)
        
    return render_template('general.html', title='Home', avg = avg, numUser = numUser, shortqmarks = shortqmarks, shortqpercent = shortqpercent, avglong = avglong, longqmark = longqmark, longqpercent = longqpercent, numUserlonganswer= numUserlonganswer)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # make sure user is not logged in already
    if current_user.is_authenticated:
        return redirect(url_for('general'))
    form = LoginForm()
    if form.validate_on_submit():
        # getting the user from the form and filtering
        # from the User database table to check for available users
        user = User.query.filter_by(username=form.username.data).first()
        # if user can't be found or password in the database is incorrect
        # show a flash msg on the client to prompt retry login
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password!')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        # getting the next page request
        next_page = request.args.get('next')
        # if login URL doesn't have a next argument
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('general')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    # make sure user is not logged in already
    if current_user.is_authenticated:
        return redirect(url_for('general'))
    form = RegistrationForm()
    # creates new user with username, email and password provided
    # writes to the database then redirects to login prompt for user to login
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('general'))

# account page which displays the marks for the short answers the feeback box and the long 
# answer marks and responses once reviewed by the admin
@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():

    # if no feedback form has been submitted previously add a feedback table relation
    # for the currentuser and if it has been submitted previously reset the feedback form
    if request.method == "POST":
        feedbackrequest = request.form["feedback"]
        if not bool(Feedbacks.query.filter_by(user_id = current_user.id).first()):
            feedback = Feedbacks(feedback_user = current_user)
            db.session.add(feedback)
            db.session.commit()
        current_user.feedback.filter_by(user_id = current_user.id).first().feedback_msg = feedbackrequest
        db.session.commit()

    # variables to store the short answer question mark, sum of the total short question marks 
    # and percentage for the mark
    current_result = ""
    question_sum = ""
    percentage = ""
    # calculate the above variables below if result can be found for the current user
    if bool(Quiz.query.filter_by(user_id = current_user.id).first()):
        question_sum = db.session.query(func.sum(Question.mark_for_question)).filter_by(long_question = False).scalar()
        current_result = current_user.quiz[0].result
        percentage = int((current_result/question_sum) *100)
    

    # querie to get a list of long answer questions
    long_questions = Question.query.filter_by(long_question = True)
    # variables for the total mark for the long question gotten, total mark weighting 
    # for the long questions, percentage for the mark and the response from admin
    quizincompleteflag = False
    markflag = False
    mark = 0
    question_mark = 0
    long_percentage = ""
    long_responses = ""
     # calculate the above variables below for each long answer question
    for question in long_questions:
        # if no long answer entry can be found for the current user then skip the loop
        if not bool(current_user.long_answer.first()):
            quizincompleteflag = True
            break
        if bool(current_user.long_answer.filter_by(question_id = question.id).first().mark != None):
            markflag = True
            mark += current_user.long_answer.filter_by(question_id = question.id).first().mark
            question_mark += question.mark_for_question
    # if there are entries in the long answer for the current user
    if not quizincompleteflag:
        long_responses = current_user.long_answer    
    # percentage for the long answers
    if question_mark != 0:
        long_percentage = int((mark/question_mark) *100)    
    return render_template('account.html', title='Account', result = current_result, sum = question_sum, percentage = percentage, mark = mark, markflag = markflag, question_mark = question_mark,long_percentage = long_percentage, quizincompleteflag = quizincompleteflag, long_responses = long_responses)


# quiz route for quiz.html the page where users get to play the quiz
@app.route('/quiz', methods=['GET', 'POST'])
@login_required
def quiz():
    
    # querie to get a list of short answer questions
    short_questions = Question.query.filter_by(long_question = False)
    # querie to get a list of long answer questions
    long_questions = Question.query.filter_by(long_question = True)
    result = 0 

    # if the quiz form on quiz.html has been submitted
    if request.method == "POST":

        # check if the answer submitted are correct for the short answer questions and generate the result accordingly
        for question in short_questions:
            strqid = str(question.id)
            request_name = request.form[strqid]
            if Option.query.filter_by( option_body = request_name).first().correct:
                result += 1

        #check if quiz has been done by a user previously if not add a quiz table for the result of the user
        if not bool(Quiz.query.filter_by(user_id = current_user.id).first()):
            quiz = Quiz(usersesh = current_user)
            db.session.add(quiz)
            db.session.commit()
        current_user.quiz[0].result = result
        db.session.commit()    

        # check if a long answer question has been answered in the past if not then add it, if so reset all responses and marks
        for question in long_questions:
            strqid = str(question.id)
            longAnswer = request.form[strqid]
            if not bool(Long_Answers.query.filter_by(user_id = current_user.id, question_id = question.id).first()):
                long_answer = Long_Answers(long_answer_user = current_user, long_question = question)
                db.session.add(long_answer)
                db.session.commit()
            dbsesh = current_user.long_answer.filter_by(question_id = question.id).first()
            dbsesh.answer = longAnswer
            dbsesh.response = None
            dbsesh.mark = None
            db.session.commit()

        return redirect(url_for('account'))

    return render_template('quiz.html', title='Quiz', short_questions = short_questions, long_questions = long_questions)


@app.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    return render_template('admin/index.html', title='Admin')


from flask import Flask, session, render_template, flash, redirect, url_for, request
from app import app, db
from datetime import timedelta
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from app.forms import LoginForm, RegistrationForm
from werkzeug.urls import url_parse

# log out user after every 5 mins of true inactivity
@app.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)
    # resets the time
    session.modified = True

@app.route('/')
@app.route('/index')
@login_required
def index():
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Tony'},
            'body': 'Today was only stressful because I looked at the work! xd'
        }
    ]
    return render_template('index.html', title='Home', posts=posts)
    # 


@app.route('/login', methods= ['GET','POST'])
def login():
    # make sure user is not logged in already
    if current_user.is_authenticated:
        return redirect(url_for('index'))
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
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html',title = 'Sign In', form = form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    # make sure user is not logged in already
    if current_user.is_authenticated:
        return redirect(url_for('index'))
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
    return redirect(url_for('index'))

    
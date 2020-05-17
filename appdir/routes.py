from flask import Flask, render_template, flash, redirect, url_for
from appdir import appvar
from appdir.forms import LoginForm



@appvar.route('/')
@appvar.route('/index')
def index():
    user = {'username': 'Miguel'}
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
    return render_template('index.html', user=user, title='Home', posts=posts)
    # 
@appvar.route('/login', methods= ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',title = 'Sign In', form = form)
    
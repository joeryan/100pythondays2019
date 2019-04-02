from flask import render_template, flash, redirect
from app import application
from app.forms import LoginForm

@application.route('/')
@application.route('/index')
def index():
  user = {'username': "Tracey"}
  posts = [
    {
      'author': {'username': 'John'},
      'body': 'Beautiful day in Michigan!'
    },
    {
      'author': {'username': 'Susan'},
      'body': 'The Avengers movie was super cool!'
    }
  ]
  return render_template('index.html', title='Home', user=user, posts=posts)

@application.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    flash('Login requested for user {}, remember_me={}'.format(
      form.username.data, form.remember_me.data))
    return redirect('/index')
  return render_template('login.html', title='Sign In', form=form)
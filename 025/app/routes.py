from flask import render_template
from app import application

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

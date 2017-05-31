from flask import render_template
from app import app

@app.route('/about')
def about():
    response = render_template('about.html')
    return response

@app.route('/')
@app.route('/index')
def index():
    #return 'Hello, World!'
    user = {'nickname': 'John'} # Fake user
    posts = [ # Fake array of posts
        {
            'author': {'nickname': 'Miguel'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    response = render_template(
        'index.html',
        title='Home',
        user=user,
        posts=posts
    )
    return response

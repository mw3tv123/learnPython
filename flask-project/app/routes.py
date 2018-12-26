from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Hung'}
    posts = [
        {
            'author': {'username': 'Nick'},
            'body': 'Beautiful day in England!'
        },
        {
            'author': {'username': 'Niko'},
            'body': 'Nice day for a walk!'
        },
        {
            'author': {'username': 'Reg'},
            'body': 'Keep moving into the Storm!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

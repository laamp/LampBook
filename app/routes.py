from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Lance'}
    posts = [
        {
            'author': {'username': 'Lance'},
            'body': 'Tight, tight, tight.'
        },
        {
            'author': {'username': 'Slippy'},
            'body': 'Bwop, bwop, BWAHHP'
        }
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)

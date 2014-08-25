from flask import render_template
from flask import request
from flask import flash
from app import app
from forms import LoginForm
from models import User

@app.route('/')
def index():
    user = {'nickname': 'flask'}
    posts = [{'author': 'hello',
             'body': 'world'}, {'author': 'hello','body': 'flask'}]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        name = form.username.data
        password = form.password.data
        user = User.query.filter_by(user_name=name).first()
        if user is None:
            flash('no this user!')
            return render_template('login.html', title='Login', form=form)
        else:
            if user.password != password:
                flash('password error')
                return render_template('login.html', title='Login', form=form)
            else:
                return render_template('index.html', title='Home', user=user)
    return render_template('login.html', title='Login', form=form)

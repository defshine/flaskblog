from flask import render_template
from flask import request, redirect, url_for, jsonify
from flask import flash
from app import app, login_manager
from forms import LoginForm
from models import User, Post, Category, Comment
from flask.ext.login import login_user, login_required, current_user, logout_user


@app.route('/')
def index():

    posts = [{'author': 'hello',
             'body': 'world'}, {'author': 'hello','body': 'flask'}]
    if current_user.get_id() is not None:
        user = current_user
        return render_template('index.html', title='Home', user=user, posts=posts)

    return render_template('index.html', title='Home',posts=posts)


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(user_id=user_id).first()


@app.before_request
def before_request():
    """
    if no user login, the current_user is AnonymousUserMixin object
    :return:
    """
    print current_user


@app.route('/login', methods=['GET', 'POST'])
def login():

    if current_user.get_id() is not None:
        return redirect(url_for('index'))

    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        name = form.username.data
        password = form.password.data
        remember_me = form.remember_me.data
        print remember_me
        user = User.query.filter_by(user_name=name).first()
        if user is None:
            flash('No this user !')
            return render_template('login.html', title='Login', form=form)
        else:
            if user.password != password:
                flash('Password error !')
                return render_template('login.html', title='Login', form=form)
            else:
                login_user(user, remember_me)
                return redirect(url_for('admin'))
    return render_template('login.html', title='Login', form=form)


@app.route('/admin')
@login_required
def admin():
    return render_template('admin-home.html', title='Admin', user=current_user)


@app.route('/admin/new_post')
@login_required
def admin_new_post():
    return render_template('admin-newpost.html', title='Admin', user=current_user)


@app.route('/admin/posts')
@login_required
def admin_posts():
    return render_template('admin-posts.html', title='Admin', user=current_user)


@app.route('/admin/categories')
@login_required
def admin_categories():
    return render_template('admin-categories.html', title='Admin', user=current_user)


@app.route('/admin/comments')
@login_required
def admin_comments():
    return render_template('admin-comments.html', title='Admin', user=current_user)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/categories')
@login_required
def list_category():
    return jsonify(status='200', categories=Category.list_category())

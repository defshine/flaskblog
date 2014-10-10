from flask import render_template
from flask import request, redirect, url_for, jsonify
from flask import flash
from app import app, login_manager
from forms import LoginForm, CategoryForm
from models import User, Post, Category, Comment
from flask.ext.login import login_user, login_required, current_user, logout_user
import hashlib

# pagination
POSTS_PER_PAGE = 5


@app.route('/')
@app.route('/index')
@app.route('/index/<int:page>')
def index(page=1):
    posts = Post.query.filter_by(post_status=1).paginate(page, POSTS_PER_PAGE, False)
    categories = Category.query.all()
    if current_user.get_id() is not None:
        user = current_user
        return render_template('index.html', title='Home', user=user, posts=posts, categories=categories)

    return render_template('index.html', title='Home', posts=posts, categories=categories)


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
        name = form.username.data.strip()
        password = form.password.data.strip()
        remember_me = form.remember_me.data
        m = hashlib.md5()
        m.update(password)
        user = User.query.filter_by(user_name=name).first()
        if user is None:
            flash('No this user !')
            return render_template('login.html', title='Login', form=form)
        else:
            if user.password != m.hexdigest():
                flash('Password error !')
                return render_template('login.html', title='Login', form=form)
            else:
                login_user(user, remember_me)
                return redirect(url_for('admin'))
    return render_template('login.html', title='Login', form=form)


@app.route('/admin')
@login_required
def admin():
    return render_template('admin_home.html', title='Admin', user=current_user)


@app.route('/admin/new_post')
@login_required
def admin_new_post():
    return render_template('admin_newpost.html', title='Admin', user=current_user)


@app.route('/admin/posts')
@login_required
def admin_posts():
    posts = Post.query.all()
    return render_template('admin_posts.html', title='Admin', user=current_user,posts=posts)


@app.route('/admin/post/<int:post_id>', methods=['GET'])
@login_required
def admin_get_post_by_id(post_id):
    post = Post.query.filter_by(post_id=post_id).first()
    return render_template('admin_post.html', post=post, user=current_user)

@app.route('/admin/edit_post/<int:post_id>', methods=['GET'])
@login_required
def admin_edit_post_by_id(post_id):
    post = Post.query.filter_by(post_id=post_id).first()
    categories = Category.query.all()
    category_id = post.category_id
    if int(category_id) != 0:
        category = Category.query.filter_by(cat_id=category_id).first()
        if category is not None:
            return render_template('admin_edit_post.html',
                           post=post, category=category, categories=categories, user=current_user)
        else:
            return render_template('admin_edit_post.html',
                           post=post, categories=categories, user=current_user)
    else:
        return render_template('admin_edit_post.html',
                           post=post, categories=categories, user=current_user)


@app.route('/admin/delete_post/<int:post_id>', methods=['GET'])
@login_required
def admin_delete_post_by_id(post_id):
    Post.delete(post_id)
    posts = Post.query.all()
    return render_template('admin_posts.html', title='Admin', user=current_user, posts=posts)


@app.route('/admin/categories')
@login_required
def admin_categories():
    categories = Category.query.all()
    return render_template('admin_categories.html', title='Admin', user=current_user, categories=categories)


@app.route('/admin/category', methods=['GET', 'POST'])
@login_required
def admin_category():

    form = CategoryForm()
    if request.method == 'POST' and form.validate_on_submit():
        cat_name = form.cat_name.data.strip()
        cat_description = form.cat_description.data.strip()
        Category.save(cat_name, cat_description)
        categories = Category.query.all()
        return render_template('admin_categories.html', title='Admin', user=current_user, categories=categories)

    return render_template('admin_new_category.html', title='Admin', form=form, user=current_user)


@app.route('/admin/edit_category/<int:cat_id>', methods=['GET', 'POST'])
@login_required
def admin_edit_category(cat_id):

    form = CategoryForm()
    if request.method == 'POST' and form.validate_on_submit():
        cat_name = form.cat_name.data.strip()
        cat_description = form.cat_description.data.strip()
        Category.update(cat_id, cat_name, cat_description)
        categories = Category.query.all()
        return render_template('admin_categories.html', title='Admin', user=current_user, categories=categories)
    else:
        category = Category.query.filter_by(cat_id=cat_id).first()
        form.cat_name.data = category.cat_name
        form.cat_description.data = category.cat_description
        return render_template('admin_edit_category.html', title='Admin', form=form, user=current_user)


@app.route('/admin/delete_category/<int:cat_id>', methods=['GET'])
@login_required
def admin_delete_category(cat_id):
    Category.delete(cat_id)
    posts = Post.query.filter_by(category_id=cat_id).all()
    if posts is not None:
        for p in posts:
            Post.update_category_id(p.post_id, 0)
    categories = Category.query.all()
    return render_template('admin_categories.html', title='Admin', user=current_user, categories=categories)


@app.route('/admin/comments')
@login_required
def admin_comments():
    return render_template('admin_comments.html', title='Admin', user=current_user)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/categories')
@login_required
def list_category():
    return jsonify(status='200', categories=Category.list_category())


@app.route('/post', methods=['POST'])
@login_required
def save_post():
    req_data = request.form
    post_id = req_data.get('postId')
    post_title = req_data.get('title')
    post_content = req_data.get('content')
    category_id = req_data.get('categoryId')
    post_status = req_data.get('postStatus')
    author_id = current_user.get_id()
    if post_id is not None:
        Post.update(author_id, post_title, post_content, post_status, category_id, post_id)
        return jsonify(status='200', postId=post_id)
    else:
        post_id = Post.save(author_id, post_title, post_content, post_status, category_id)
        return jsonify(status='200', postId=post_id)


@app.route('/post/<int:post_id>', methods=['GET'])
@app.route('/index/post/<int:post_id>', methods=['GET'])
@login_required
def get_post_by_id(post_id):
    post = Post.query.filter_by(post_id=post_id).first()
    categories = Category.query.all()
    return render_template('blog.html', title='Blog', post=post, categories=categories, user=current_user)

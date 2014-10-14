from flask import Blueprint, render_template, redirect, url_for
from models import Post, Category
from flask.ext.login import current_user, login_required, logout_user

bp = Blueprint('blog', __name__)

# pagination
POSTS_PER_PAGE = 5


@bp.route('/')
@bp.route('/<int:page>')
def index(page=1):
    posts = Post.query.paginate(page, POSTS_PER_PAGE, False)
    categories = Category.query.all()
    return render_template('index.html', title='Home', posts=posts, categories=categories, user=current_user)


@bp.route('/post/<int:post_id>', methods=['GET'])
def get_post_by_id(post_id):
    post = Post.query.filter_by(post_id=post_id).first()
    categories = Category.query.all()
    return render_template('blog.html', title='Blog',
                           post=post, categories=categories, user=current_user)


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('blog.index'))


@bp.route('/about')
def about():
    return render_template('about.html', title='about', user=current_user)
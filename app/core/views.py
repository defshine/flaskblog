from flask import Blueprint, render_template, redirect, url_for, request
from models import Post, Category, Blogroll
from models import cache
from flask.ext.login import current_user, login_required, logout_user
from sqlalchemy import desc

bp = Blueprint('blog', __name__)

# pagination
POSTS_PER_PAGE = 5


@bp.route('/')
@bp.route('/<int:page>')
def index(page=1):
    posts = Post.query.order_by(desc(Post.post_date)).paginate(page, POSTS_PER_PAGE, False)
    categories = Category.query.all()
    blogrolls = Blogroll.query.all()
    return render_template('index.html', title='Home',
                           posts=posts, categories=categories, blogrolls=blogrolls, user=current_user)


@bp.route('/categories/<int:category_id>/posts')
def get_post_by_category(category_id):
    page = int(request.args.get('page'))
    posts = Post.query.filter_by(category_id=category_id).order_by(desc(Post.post_date)).paginate(page, POSTS_PER_PAGE, False)
    categories = Category.query.all()
    blogrolls = Blogroll.query.all()
    return render_template('category_blog.html', title='Home',
                           posts=posts, categories=categories, blogrolls=blogrolls, user=current_user)


@cache.cached(timeout=50)
@bp.route('/posts/<int:post_id>', methods=['GET'])
@bp.route('/categories/<int:category_id>/posts/<int:post_id>', methods=['GET'])
def get_post_by_id(post_id, category_id=None):
    if category_id is not None:
        post = Post.query.filter_by(post_id=post_id, category_id=category_id).first()
    else:
        post = Post.query.filter_by(post_id=post_id).first()
    categories = Category.query.all()
    blogrolls = Blogroll.query.all()
    return render_template('blog.html', title='Blog',
                           post=post, categories=categories, blogrolls=blogrolls, user=current_user)


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('blog.index'))


@bp.route('/about')
def about():
    return render_template('about.html', title='about', user=current_user)
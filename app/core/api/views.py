from flask import jsonify
from app.core.models import Post, Category
from .import api
from sqlalchemy import desc


@api.route('/posts')
def get_posts():
    posts = Post.query.order_by(desc(Post.post_date)).all()
    return jsonify(status='200', posts=[p.to_json() for p in posts])


@api.route('/posts/<int:post_id>')
def get_posts_by_id(post_id):
    post = Post.query.filter_by(post_id=post_id).first()
    return jsonify(status='200', post=post.to_json())


@api.route('/categories/<int:category_id>/posts')
def get_posts_by_category_id(category_id):
    posts = Post.query.filter_by(category_id=category_id).order_by(desc(Post.post_date)).all()
    return jsonify(status='200', posts=[p.to_json() for p in posts])


@api.route('/categories')
def get_categories():
    cats = Category.query.all()
    return jsonify(status='200', cats=[c.to_json() for c in cats])


@api.route('/categories/<int:category_id>')
def get_categories_by_id(category_id):
    cat = Category.query.filter_by(cat_id=category_id).first()
    return jsonify(status='200', category=cat.to_json())



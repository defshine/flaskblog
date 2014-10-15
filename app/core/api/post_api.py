from app.core.models import Post
from flask.views import MethodView
from flask import jsonify, request


class PostAPI(MethodView):
    """
    Pluggable Views
    Implement the restful api for post
    """
    def get(self, post_id):
        if post_id is None:
            posts = Post.query.all()
            return jsonify(status='200', posts=[p.to_json() for p in posts])
        else:
            post = Post.query.filter_by(post_id=post_id).first()
            return jsonify(status='200', post=post.to_json())

    # for test but no use
    def post(self):
        form = request.form
        return jsonify(status='200')



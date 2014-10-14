from flask import Blueprint

bp = Blueprint('blog', __name__)


@bp.route('/')
def hello_world():
    return '<a href="/admin/">Click me to get to Admin!</a>'
from post_api import PostAPI


def register_api(app):
    """
    Register restful api
    :param app: flask app
    :return:
    """
    post_view = PostAPI.as_view('post_api')
    app.add_url_rule('/posts/', defaults={'post_id': None},  view_func=post_view, methods=['GET', ])
    app.add_url_rule('/posts/', view_func=post_view, methods=['POST', ])
    app.add_url_rule('/posts/<int:post_id>', view_func=post_view, methods=['GET'])

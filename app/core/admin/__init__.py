from flask.ext.admin import Admin
from app.core.models import User, Post, Category, Blogroll
from app.core.admin.views import AdminUserView, AdminIndexView, AdminPostView, AdminCategoryView, AdminBlogrollView


def create_admin(app=None, db=None):
    admin = Admin(app, 'BlogAdmin', index_view=AdminIndexView(), base_template='admin/my_master.html')
    admin.add_view(AdminUserView(User, db.session))
    admin.add_view(AdminPostView(Post, db.session))
    admin.add_view(AdminCategoryView(Category, db.session))
    admin.add_view(AdminBlogrollView(Blogroll, db.session))

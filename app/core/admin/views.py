from flask.ext.admin.contrib import sqla
from flask.ext.login import current_user, login_user, logout_user
from flask.ext.admin import expose, helpers, AdminIndexView
from flask import redirect, url_for, request
from wtforms import fields, widgets, validators
from forms import LoginForm


class AdminIndexView(AdminIndexView):

    @expose('/')
    def index(self):
        if not current_user.is_authenticated():
            return redirect(url_for('.login'))
        return super(AdminIndexView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login(self):
        form = LoginForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = form.get_user()
            login_user(user)

        if current_user.is_authenticated():
            return redirect(url_for('.index'))
        # link = '<p>Don\'t have an account? <a href="' + url_for('.register_view') + '">Click here to register.</a></p>'
        self._template_args['form'] = form
        # self._template_args['link'] = link
        return super(AdminIndexView, self).index()

    @expose('/logout/')
    def logout_view(self):
        logout_user()
        return redirect(url_for('.index'))


class AdminUserView(sqla.ModelView):

    column_display_pk = True
    can_create = False

    # Override displayed fields
    column_list = ('user_id', 'user_name', 'user_qq', 'user_mail', 'password')
    column_labels = dict(user_id='Id', user_name='Name', user_qq='QQ', user_mail='Mail', password='Password')

    def is_accessible(self):
        return current_user.is_authenticated()


# Define wtforms widget and field
class CKTextAreaWidget(widgets.TextArea):
    def __call__(self, field, **kwargs):
        kwargs.setdefault('class_', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)


class CKTextAreaField(fields.TextAreaField):
    widget = CKTextAreaWidget()


# Customized admin interface
class AdminPostView(sqla.ModelView):

    form_overrides = dict(post_content=CKTextAreaField)

    form_columns = ('post_title', 'category', 'post_content')

     # Override displayed fields
    column_list = ('post_id', 'author', 'category', 'post_title', 'post_content', 'post_date')
    column_labels = dict(post_id='Id', author='author', category='Category', post_title='Title',
                         post_content='content', post_date='Post date')

    column_filters = ('post_title', 'post_content')
    # add form validate
    form_args = dict(
        post_title=dict(label='Title', validators=[validators.required()]),
        category=dict(label='Category', validators=[validators.required()]),
        post_content=dict(label='Content', validators=[validators.required()]))

    create_template = 'admin/create_post.html'
    edit_template = 'admin/edit_post.html'

    def is_accessible(self):
        return current_user.is_authenticated()


class AdminCategoryView(sqla.ModelView):

    column_display_pk = True

    # Enable model creation
    can_create = True

    # Override displayed fields
    column_list = ('cat_id', 'cat_name', 'cat_description')
    column_labels = dict(cat_id='Id', cat_name='Category Name', cat_description='Category Description')

    form_columns = ('cat_name', 'cat_description')

    column_filters = ('cat_name', 'cat_description')
    # add form validate
    form_args = dict(
        cat_name=dict(label='Category Name', validators=[validators.required()]),
        cat_description=dict(label='Category Description', validators=[validators.required()]))

    def is_accessible(self):
        return current_user.is_authenticated()


class AdminBlogrollView(sqla.ModelView):

    column_display_pk = True

    # Enable model creation
    can_create = True

    # Override displayed fields
    column_list = ('br_id', 'br_name', 'br_url')
    column_labels = dict(br_id='Id', br_name='Blogroll Name', br_url='Blogroll Url')

    form_columns = ('br_name', 'br_url')

    column_filters = ('br_name', 'br_url')
    # add form validate
    form_args = dict(
        cat_name=dict(label='Blogroll Name', validators=[validators.required()]),
        cat_description=dict(label='Blogroll Url', validators=[validators.required()]))

    def is_accessible(self):
        return current_user.is_authenticated()






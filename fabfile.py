from fabric.api import *


env.hosts = ['172.19.3.123']
env.user = 'xin'
env.password = '1201027'


def add():
    local("git add .")


def commit():
    local("git add -p && git commit")


def push():
    local("git push")


def first_deploy():
    code_dir = '/home/xin/www'
    with cd(code_dir):
        run("git clone https://github.com/defshine/flaskblog.git")


def deploy():
    code_dir = '/home/xin/www'
    with cd(code_dir):
        run("git pull")
        run("gunicorn -b 0.0.0.0:8005 run:app")
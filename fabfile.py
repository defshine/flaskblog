from fabric.api import *


env.hosts = ['']
env.user = ''
env.password = ''


#clone code from github
def clone():
    code_dir = '/home/xin/www'
    with cd(code_dir):
        run("git clone https://github.com/defshine/flaskblog.git")


#update project
def update():
    code_dir = '/home/xin/www/flaskblog'
    with cd(code_dir):
        run("git pull")


#restart project
def restart():
    sudo("supervisorctl restart flaskblog")
    sudo("supervisorctl status")


#check the project status
def check():
    sudo("supervisorctl status")




flaskblog
=========

New dev branch  
Learn python and flask,just a tony blog system  
It is same as [SpringBlog](https://github.com/defshine/SpringBlog),but implemented differently    

#Use:  
  
##Backend:
  1. [Flask](http://flask.pocoo.org/)
  2. [Flask-SQLAlchemy](https://pythonhosted.org/Flask-SQLAlchemy/) ORM for mysql  
  3. [Flask-WTF](https://flask-wtf.readthedocs.org/en/latest/)
  4. [Flask-Login](https://flask-login.readthedocs.org/en/latest/)  
  5. [Flask-Admin](http://flask-admin.readthedocs.org/en/latest/)

##Web:
  1. Jquery-1.11.1
  2. Bootstrap-3.2.0  
  3. Very simple editor [qeditor](https://github.com/huacnlee/jquery.qeditor)

#Finish:  
The basic function of blog:  
  
> Post:read,write,edit,delete  
> Category:read,add,edit,delete  
> Comment:read,add,delete

#Todo:  
1. Review python code and think more
2. Write front with AngularJS instead of jQuery  
3. Use Flask-Admin  
4. Develop restful api    
5. Develop simple android app

#Deploy  
Create Schema on MySql,edit database setting in config.py    
Then run init_db.py to init database  

Use gunicorn and supervisor to deploy this project on Ubuntu    
Install gunicorn and supervisor:  

> $ sudo pip install gunicorn  
> $ sudo pip install supervisor  

Copy supervisor config file:  

> $ sudo cp flaskblog.conf /etc/supervisor/conf.d/ 

Restart supervisor and start flaskblog:  
  
> $ sudo supervisorctl reload  
> $ sudo supervisorctl start flaskblog  

Look status:  

> $ sudo supervisorctl status

#Connect me
Life is short,you need python!
if you are interested in this project, Join us!

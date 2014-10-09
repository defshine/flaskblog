flaskblog
=========

Learn python and flask,just a tony blog system  
It is same as [SpringBlog](https://github.com/defshine/SpringBlog),but implemented differently    

#Use:  
  
##Backend:
  1. [Flask](http://flask.pocoo.org/)
  2. [Flask-SQLAlchemy](https://pythonhosted.org/Flask-SQLAlchemy/) ORM for mysql  
  3. [Flask-WTF](https://flask-wtf.readthedocs.org/en/latest/)
  4. [Flask-Login](https://flask-login.readthedocs.org/en/latest/)  

##Web:
  1. Jquery-1.11.1
  2. Bootstrap-3.2.0  

#Finish:    
1. Login and remember me, user Flask-login  
2. Admin Home
3. Publish and save post
4. Show blog list in index
5. Show blog content

#Todo:
1. Finish the basic blog function
2. Review python code and think more
3. Write front with AngularJS instead of jQuery  

#Deploy

User gunicorn and supervisor to deploy this project on Ubuntu    
Install gunicorn:  

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

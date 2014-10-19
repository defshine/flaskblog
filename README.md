flaskblog
=========

Learn python and flask,just a tony blog system  
It is same as [SpringBlog](https://github.com/defshine/SpringBlog),but implemented differently  
New branch dev to develop restful api
  
###Version:v0.2-dev  

##Use:    
  
###Backend:  

  1. [Flask](http://flask.pocoo.org/)
  2. [Flask-SQLAlchemy](https://pythonhosted.org/Flask-SQLAlchemy/) ORM for mysql  
  3. [Flask-WTF](https://flask-wtf.readthedocs.org/en/latest/)
  4. [Flask-Login](https://flask-login.readthedocs.org/en/latest/)  
  5. [Flask-Admin](http://flask-admin.readthedocs.org/en/latest/)  
  6. [Flask-Script](http://flask-script.readthedocs.org/en/latest/)

###Web:  
  
  1. [Bootstrap-3.2.0](http://getbootstrap.com/)    
  2. [CKEditor](http://ckeditor.com/)

##Finish:   
  
1. Review python code and change project directory structure  
2. The basic function of blog:  
  
 > Post:read,write,edit,delete  
 > Category:read,add,edit,delete  
  
3. Use pluggable views develop simple restful api  

 <table>
    <tr>
        <td>URL</td>
        <td>Method</td>
        <td>Description</td>
    </tr>
    <tr>
        <td>/posts/</td>
        <td>GET</td>
        <td>Gives a list of all posts</td>
    </tr>
    <tr>
        <td>/posts/post_id</td>
        <td>GET</td>
        <td>Gives a posts by post_id</td>
    </tr>   
 </table>  
   
##Todo   
    
1. Develop simple android app

##Deploy  
    
Pelease see project wiki [Deploy Flask App on Ubuntu with Gunicorn,Nginx,Supervisor](https://github.com/defshine/flaskblog/wiki/Deploy-Flask-App-on-Ubuntu-with-Gunicorn,Nginx,Supervisor)  
  

## Version  

v0.2  
v0.1    
 
##Connect me  

Life is short,you need python!
If you are interested in this project, Join us!  

## License  

This project is licensed under the [MIT license](http://opensource.org/licenses/MIT), see `LICENSE` for more details.

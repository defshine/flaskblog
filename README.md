flaskblog
=========

Learn python and flask,just a tony blog system based on flask and mysql  
It is similar to [cleanblog](https://github.com/defshine/cleanblog), a blog system based on flask and mongoengine  


###Version:v0.2-dev  

##Use:    
  
###Backend:  

  1. [Flask](http://flask.pocoo.org/)
  2. [Flask-SQLAlchemy](https://pythonhosted.org/Flask-SQLAlchemy/) ORM for mysql  
  3. [Flask-WTF](https://flask-wtf.readthedocs.org/en/latest/)
  4. [Flask-Login](https://flask-login.readthedocs.org/en/latest/)  
  5. [Flask-Admin](http://flask-admin.readthedocs.org/en/latest/)  
  6. [Flask-Script](http://flask-script.readthedocs.org/en/latest/)  
  7. [Flask-Cache](http://www.pythondoc.com/flask-cache/index.html)  
  
###Web:  
  
  1. [Bootstrap-3.2.0](http://getbootstrap.com/)  
  2. [bootstrap-material-design](https://github.com/FezVrasta/bootstrap-material-design)      
  3. [CKEditor 4.4.7_standard](http://ckeditor.com/)

##Finish:   
  
####The basic function of blog:  
  
 > Post:read,write,edit,delete  
 > Category:read,add,edit,delete  
 > Comment: use duoshuo  
 > Blogroll: add,list
     
####Develop simple restful api  

 <table>
    <tr>
        <td>URL</td>
        <td>Method</td>
        <td>Description</td>
    </tr>
    <tr>
        <td>/api/posts</td>
        <td>GET</td>
        <td>Gives a list of all posts</td>
    </tr>
    <tr>
        <td>/api/posts/post_id</td>
        <td>GET</td>
        <td>Gives a posts by post_id</td>
    </tr>
     <tr>
        <td>/api/categories/category_id/posts</td>
        <td>GET</td>
        <td>Gives a list of posts by category_id</td>
    </tr>  
     <tr>
        <td>/api/categories</td>
        <td>GET</td>
        <td>Gives a list of all categories</td>
    </tr>
    <tr>
        <td>/api/categories/category_id</td>
        <td>GET</td>
        <td>Gives a categories by category_id</td>
    </tr> 
 </table>  
   
##Todo   
    
1. Think more about restful api design  
2. Develop simple android app

##Deploy  
    
Pelease see project wiki [Deploy Flask App on Ubuntu(Virtualenv+Gunicorn+Nginx+Supervisor)](https://github.com/defshine/flaskblog/wiki/Deploy-Flask-App-on-Ubuntu(Virtualenv-Gunicorn-Nginx-Supervisor))  
  

## Version  

v0.2  
v0.1    
 
##Connect me  

Life is short,you need python!
If you are interested in this project, Join us!  

## License  

This project is licensed under the [MIT license](http://opensource.org/licenses/MIT), see `LICENSE` for more details.

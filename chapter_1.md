# Chapter 1
## Building a Blog Application
1. Creating my project 
    >django-admin startproject mysite
    - Running the development server
        > python3 manage.py runserver
    - Project settings
2. Creating blog application inside my project
   > python3 manage.py startapp blog <br/>
    - Activating the application by adding blog app details to mysite/setting.py
    - Creating model by updating blog/models.py  and appling makemigrations and migrate command.
        > python3 manage.py makemigrations app name- optionsl
        > python3 manage.py migrate 
3. Creating Administration site for models 
    - Creating superuser
        > python3 manage.py createsuperuser
        - create username and password for admins
    - Adding models to the administration site
    - Customize the way the models are displayed
        * created templates folder inside blog and created base.html for base tmeplate
        * created post folder in templates and created views for list.html and details.html using django framework template tags
        *  Created blog/templates/pagination.html for paging the view of the application
    - for styling, created static folder in blog and static/css/blog.css
4. Files created and updated
    * mysite/setting.py
    * mysite/urls.py
    * mysite/blog/admin.py
    * mysite/blog/models.py
    * mysite/blog/views.py
    * mysite/blog/urls.py
    * mysite/blog/templates/base.html
    * mysite/blog/templates/blog/post/list.html
    * mysite/blog/templates/blog/post/details.html
    * mysite/blog/templates/pagination.html
    * mysite/blog/static/css/blog.css
    
  
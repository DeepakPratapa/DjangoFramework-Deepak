1.  Create a Virtual Environment

a. Use the following code for a version       
   python3.11 -m venv myenv     

b. Activate the scripts ; go to the scripts folder   
         ./activate

c.Install the requirements.txt 
    pip install -r requirements.txt 


2. Django 

a.Create a django Project  
      django-admin startproject *AnyName

b. Use this to open and migrate the server
    python manage.py migrate
    
    Then run the server
    python manage.py runserver

c. Start the django app
     django-admin startapp testing

d. Now we need to register this file in settings.py

        '*appname',

e. Create and connect url.py and view.py
   We are trying to connect the  app
   to django project.

    Open urls.py in the project and  add 

        from django.urls import path,include
        path('',include('testing.urls'))

        Now we will be able to create urls in the app itself

f. Update views to add the required pages.

g. After setting up the app , now we need to restrict access .


3. OpenSSL 

 a. As we are using this as a Development Server 
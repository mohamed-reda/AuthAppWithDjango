##commands

1
pipenv install django~=3.1.14
pip install django  

~= which will ensure security updates for Django, such as 3.1.1, 3.1.2, and so on.

------------------------------------------------------------------------------

check

django-admin --version

------------------------------------------------------------------------------

activate virtual environment:

pipenv shell

------------------------------------------------------------------------------

if this runs with no error:

2

django-admin startproject smartnotes .

so my virtual environment has Django installed properly.

here without (.) to the command, it will create config folder in config folder

------------------------------------------------------------------------------

3

django-admin startapp home

django-admin startapp notes

------------------------------------------------------------------------------

running Django’s local web server 

python manage.py runserver

exit

------------------------------------------------------------------------------

pipenv shell

exit


------------------------------------------------------------------------------

python manage.py startapp pages

• admin.py is a configuration file for the built-in Django Admin app

• apps.py is a configuration file for the app itself

• migrations/ keeps track of any changes to our models.py file so our database and models.py stay in sync

• models.py is where we define our database models which Django automatically translates into database tables

• tests.py is for our app-specific tests

• views.py is where we handle the request/response logic for our web app

------------------------------------------------------------------------------
Run:

python manage.py runserver

------------------------------------------------------------------------------
test:

python manage.py test

------------------------------------------------------------------------------

apply the migrations:

python manage.py migrate

change the user:


python manage.py createsuperuser

nilecrocodile

mohamed.reda.007007@gmail.com
12345678

------------------------------------------------------------------------------
after creating new model at notes, lets deal with the database:

python manage.py makemigrations

------------------------------------------------------------------------------

apply the migrations:

python manage.py migrate

------------------------------------------------------------------------------


python manage.py shell

from notes.models import Notes

mynote = Notes.objects.get(pk='1')

mynote.title

to access all database 

mynote = Notes.objects.all()

 mynote[0].title

------------------------------------------------------------------------------
create new

new_note = Notes.objects.create(title='second',text='text2')

new_note = Notes.objects.create(title='second2',text='text22')



filter

l= Notes.objects.filter(text__startswith='text')

l= Notes.objects.filter(text__contains='what')


not having the word:

l= Notes.objects.exclude(text__contains='what')


not have 'what' but have 'text'

l= Notes.objects.exclude(text__contains='what').filter(text__startswith='text22')

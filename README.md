## Note app With Django Framwork

Ths is a working system that can create, edit, and list books per user with an authentication system.

It has:
- creating users and data 
- dealing with ORMs and store the data using SQlite Database
- creating a dynamic template
- dealing with Django Admin
- Django class-based files and static views, and so much more!

## Screenshots


create note Page:

<img src="https://github.com/mohamed-reda/NoteAppWithDjango/blob/master/images/create%20note.png?raw=true"  width="800" height="400" />  


<img src="https://github.com/mohamed-reda/NoteAppWithDjango/blob/master/images/home.png?raw=true"  width="800" height="400" />  


logout :  

<img src="https://github.com/mohamed-reda/NoteAppWithDjango/blob/master/images/logout.png?raw=true" width="800" height="400"  />  



Notes for new User:

<img src="https://github.com/mohamed-reda/NoteAppWithDjango/blob/master/images/notes%20for%20new%20user.png?raw=true" width="800" height="400"  />  

Notes Page:

<img src="https://github.com/mohamed-reda/NoteAppWithDjango/blob/master/images/notes.png?raw=true" width="800" height="400"  />  

signup Page:

<img src="https://github.com/mohamed-reda/NoteAppWithDjango/blob/master/images/signup.png?raw=true" width="800" height="400"  />  

single note:

<img src="https://github.com/mohamed-reda/NoteAppWithDjango/blob/master/images/single%20note.png?raw=true" width="800" height="400"  />  

login:

<img src="https://github.com/mohamed-reda/NoteAppWithDjango/blob/master/images/the%20login.png?raw=true" width="800" height="400"  />  

create note:

<img src="https://github.com/mohamed-reda/NoteAppWithDjango/blob/master/images/create%20note.png?raw=true" width="800" height="400"  />  

edit with error:

<img src="https://github.com/mohamed-reda/NoteAppWithDjango/blob/master/images/edit%20with%20error.png?raw=true" width="800" height="400"  />  

edit without error:

<img src="https://github.com/mohamed-reda/NoteAppWithDjango/blob/master/images/edit%20without%20error.png?raw=true" width="800" height="400"  />  

dealing with Django Admin:

<img src="https://github.com/mohamed-reda/NoteAppWithDjango/blob/master/images/admin.png?raw=true" width="800" height="400"  />  
<img src="https://github.com/mohamed-reda/NoteAppWithDjango/blob/master/images/admin2.png?raw=true" width="800" height="400"  />  
<img src="https://github.com/mohamed-reda/NoteAppWithDjango/blob/master/images/admin3.png?raw=true" width="800" height="400"  />  



## commands

1 pipenv install django~=3.1.14 pip install django

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

mohamed.reda.007007@gmail.com 12345678

------------------------------------------------------------------------------
after creating new model at notes, lets deal with the database:

python manage.py makemigrations

after showing the migration of which user who created the note, apply the default athe terminal as:

1

1

then

python manage.py migrate

check:

python manage.py shell

from django.contrib.auth.models import User

user = User.objects.get(pk=1)

user

user.notes.count()

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

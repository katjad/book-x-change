# book-x-change

# Backend setup
- install python3 and django in virtualenv (https://www.digitalocean.com/community/tutorials/how-to-install-django-and-set-up-a-development-environment-on-ubuntu-16-04)
- `cd book-x-change/backend/x-change-server/`
- `python3 manage.py migrate`
- `python3 manage.py createsuperuser`
- `python3 manage.py loaddata books/fixtures/*`
- `python3 manage.py runserver`

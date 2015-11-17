# [Framgia Training System] TMS

Project training how to use django

Demo: [http://mooc-framgia.herokuapp.com/](http://mooc-framgia.herokuapp.com/)

## Installation

* [Environment](http://askubuntu.com/questions/244641/how-to-set-up-and-use-a-virtual-python-environment-in-ubuntu)

## Usage

1. Create virtualenv
    * mkvirtualenv name_virtualenv
    * workon name_virtualenv
2. Install environment with requirements.txt
    * pip install requirements.txt
3. Migrate database
    * python manage.py migrate
4. Create superuser
    * python manage.py createsuperuser (user login admin)
5. Copy file and folder in folder data_test to folder root.
6. Dumpdata and loaddata
    * python manage.py dumpdata > [name.json]
    * python manage.py loaddata [name.json]
7. Run
    * python manage.py runserver [port] (default: 8000)

## Teachers
    1. Singin, singout
    2. CRUD courses
    3. Add teacher to control course
    4. Create subject for course
    5. Create tasks for a subject (have deadline)
    6. Prevent users register subjects
    7. Post blogs.

## Students
    1. Signin, singnout, update profile, change password
    2. List subjects by catalogue
    3. View profile teacher create subject
    4. View all profile students join subject
    5. Can rate and review subject
    6. Register subject
    7. View task of subjects

## License

Framgia VN

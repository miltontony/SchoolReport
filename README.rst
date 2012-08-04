SchoolReport
============

An application that allows learners to report issues in their school
and to mobilise an appropriate response. It includes a simple
ticketing system and information portal for each school.

To get up and running locally::

    $ virtualenv --no-site-packages ve/
    $ source ve/bin/activate
    (ve)$ pip install -r requirements.pip
    (ve)$ export DJANGO_SETTINGS_MODULE=schoolreport.settings
    (ve)$ export PYTHONPATH=.
    (ve)$ django-admin.py syncdb
    (ve)$ django-admin.py migrate schoolreport
    (ve)$ django-admin.py runserver

Good luck!

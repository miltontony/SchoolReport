SchoolReport
============

An application that allows learners to report issues in their school
and to mobilise an appropriate response. It includes a simple
ticketing system and information portal for each school.

To get up and running locally::

    $ virtualenv --no-site-packages ve/
    $ source ve/bin/activate
    (ve)$ pip install -r requirements.pip
    (ve)$ cd schoolreport
    (ve)$ ./manage.py syncdb --noinput
    (ve)$ ./manage.py migrate
    (ve)$ ./manage.py loaddata ../data/export.json
    (ve)$ ./manage.py createsuperuser
    (ve)$ ./manage.py runserver

If you get this error:
	unknown locale: UTF-8

Try this::

	(ve)$ export LC_CTYPE=en_US.UTF-8
	(ve)$ export LC_ALL=en_US.UTF-8

Good luck!

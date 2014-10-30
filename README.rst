app-name
=======================

One line description

Introduction
------------

[...]

Requirements
------------

[...]

Technical details
-----------------

[...]

Installation
------------

[...]

Tests
-----

The app installer contains a test suite that can be run using the Django
test runner:

.. code:: shell

    $ pip install -r requirements.txt
    $ python manage.py test

If you want to test coverage you'll need to add some dependencies:

.. code:: shell

    $ pip install coverage django-coverage
    # add django_coverage to the INSTALLED_APPS in settings.py
    $ python manage.py test_coverage

The tests also run using `tox <https://testrun.org/tox/latest/>`_:

.. code:: shell

    $ pip install tox
    $ tox

Usage
-----

[...]

Configuration
-------------

[...]

Licence
-------

MIT (see LICENCE)

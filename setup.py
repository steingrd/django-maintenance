#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

django_maintenance_packages = [
    'maintenance',
]

long_description = """
==================
django-maintenance
==================

django-maintenance lets you define maintenance windows as objects. These 
maintenance windows are time slots where your website or parts of it is 
non-operational. django-maintenance ships with a middleware that lets you
display a friendly message to your users during the downtime.

Installing
==========
Please refer to `INSTALL.markdown` for installation instructions. Notice the
last section on configuring Django and ensure that you have the correct
settings in `INSTALLED_APPS` and `MIDDLEWARE_CLASSES`. 

Using
=====
Usage instructions can be found in `docs/overview.markdown` which is also
available online. """ + "\n\n" + open('CHANGELOG.txt').read()

setup(name='django-maintenance',
      version='0.1',
      author='Steingrim Dovland',
      author_email='steingrd@ifi.uio.no',
      url='http://wiki.github.com/steingrd/django-maintenance',
      description='Schedules planned downtime and shuts down your Django site',
      long_description=long_description,
      packages=django_maintenance_packages,
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python'])

# Installing django-maintenance #

In order to use django-maintenance you'll need a functional installation of Django
1.0 or later.

There are several ways to install django-maintenance: using a package
management tool such as `easy_install` or `pip`, or manually installing a
Python package from a source code tarball or a Github checkout.

After the Python package has been installed you'll need to configure your
Django project to use django-maintenance. Please refer to the usage
instructions in `docs/overview.markdown` for details on configuring your
Django project.

## About this document ##

This document is written in the Markdown format and contains some inline HTML.
This document is also available online at
[http://github.com/steingrd/django-maintenance/blob/master/INSTALL.markdown][install].

  [install]: http://github.com/steingrd/django-maintenance/blob/master/INSTALL.markdown

## Installing with `easy_install` ##

The easiest way to install django-maintenance is to use a Python package
management tool such as [`easy_install`][easy] or [`pip`][pip]. If you are not
familiar with such tools, now might be a good time to get started using them.

Once one of these tools are up and running you should be able to install
django-maintenance by executing a single command.

For `easy_install`:

    $ easy_install django-maintenance

Or if you prefer `pip`:

    $ pip install django-maintenance

  [easy]: http://peak.telecommunity.com/DevCenter/EasyInstall
  [pip]: http://pypi.python.org/pypi/pip/

## Installing from source code ##

If you prefer to manually install packages or to use `distutils` from the
command line you can download the latest stable version of django-maintenance
from [http://wiki.github.com/steingrd/django-maintenance][wiki].

Extract the downloaded file, inside the directory named `django-maintenance`
you'll find a directory named `maintenance`. Either move (or symlink) this
directory to somewhere on you Python path, or execute the `setup.py` script by
running:

    $ python setup.py install

Keep in mind that this command installs the package at a system-wide location
and probably needs elevated privileges.

If you have Git installed on your computer, a complete copy of the
django-plist repository can be checked out from Github by typing:

    $ git clone git://github.com/steingrd/django-maintenance.git

The instructions for installing from a source code tarball applies to a Git
checkout as well.

  [wiki]: http://wiki.github.com/steingrd/django-maintenance


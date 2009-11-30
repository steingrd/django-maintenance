# django-maintenance #

## About this document ##

This document is written in the Markdown format and contains some inline HTML.
The document is also available online at 
[http://github.com/steingrd/django-maintenance/blob/master/docs/overview.markdown][ghpage].

  [ghpage]: http://github.com/steingrd/django-maintenance/blob/master/docs/overview.markdown

## Installing django-maintenance ##

Please refer to [`INSTALL.markdown`][install] for installation instructions.
Notice the last section on configuring Django and ensure that you have the
correct settings in `INSTALLED_APPS` and `MIDDLEWARE_CLASSES`.

  [install]: http://github.com/steingrd/django-maintenance/blob/master/INSTALL.markdown

## Using django-maintenance ##

django-maintenance lets you define maintenance windows as objects. These
maintenance windows are time slots where your website or parts of it is
non-operational. django-maintenance ships with a middleware that lets you
display a friendly message to your users during the downtime.

You use `django.contrib.admin` to define maintenance objects at runtime.

### A note on performance ###

django-maintenance operates by inspecting each request and determining whether
it should be handled as a normal request or if that part of the website is
down for maintenance. If a maintenance object has been defined a template is
rendered instead of invoking the original view.

django-maintenance achieves this by using a middleware class that inspects
every incoming request. This comes with some overhead; each and every request
invokes a query against the database to check whether there is a maintenance
object defined. If performance is important and you know for sure that no
maintenance downtime is needed, you can disable the middleware in your
configuration.

### Configuring your Django project to use django-maintenance ###

Since django-maintenance depends on `django.contrib.admin` for defining
maintenance objects, your project needs to be configured to use
`django.contrib.admin`. Consult the official Django documentation for details
on adding the admin to your project.

To configure your Django project for django-maintenance, follow these four
steps:

1. Add `maintenance` to `settings.INSTALLED_APPS`:

        INSTALLED_APPS = (
            'django.contrib.admin',
            ...
            'maintenance',
        )

2. Add the `maintenance.middleware.MaintenanceMiddleware` to
  `settings.MIDDLEWARE_CLASSES`:

        MIDDLEWARE_CLASSES = (
            # other middleware classes used by Session and Auth
		    ...
		    'maintenance.middleware.MaintenanceMiddleware',
        )

3. Run `manage.py syncdb` to create the tables used by django-maintenance.
   This creates two tables `maintenance_maintenance` and
   `maintenance_maintenancefilter`.

4. Define the `maintenance/downtime.html` template that is rendered whenever
   maintenance occurs. See the next section for details on the context given
   to this template.

That's it, you are now ready to use django-maintenance.

### The `maintenance/downtime.html` template ###

When the maintenance middleware finds an active maintenance object, it aborts
the request. Instead of invoking the view and returning whatever the original
view wanted to return, it renders a special template.

You need to define the template `maintenance/downtime.html` and place it
somewhere in your `TEMPLATE_DIRS`.

This template is rendered with a context containing the maintenance object
that aborted the original request. Attributes of interest in this object are:

* `description` --- This is the textual description given in the admin.
  Usually you'll want to write why the request was aborted and when the user
  can expect to come back.

* `start_time` --- This is the `DateTimeField` that defines that start of the
  maintenance window.

* `end_time` --- This is the `DateTimeField` that defines the end of the
  maintenance window.

### Using the admin to define maintenance objects ###

To lock down parts of your website, log in to the admin and choose the
Maintenance application. Define a maintenance object by filling in the start
time, end time and a description. Make sure you check the enabled field to
activate the maintenance object. 

The middleware that intercepts the request checks the `request.path` attribute
against the list of paths defined in the maintenance object.

If no additional paths are defined, only `/admin` is allowed.

If paths are added, the `request.path` attribute is checked to see whether
they match, with the `startswith` method. 

For example, the request path `/blog/my-article/` is intercepted if the path
is `/blog/`, `/blog` or even `/b`.



# Django boilerplate
This is my prefered setup when I kick-off a new Django project!
By default it focuses on generalizing as much of the configuration OOB,
leaving configurable settings separated to development,testing,staging and
production environments.

This boilerplate also implements some basic but important security practises,
not to include credentials or any other information that could compromise the
security of the projects environment.

## Usage
Assuming you have already installed django systemwide, all you have to do (from
commandline) is to run 

```bash
django-admin.py startproject -e py,txt --template=https://https://github.com/wolfhechel/django-boilerplate/archive/master.zip Project Name <Optional path>
```

From here you're free to modify or re-configure any files you may like!

## Important files

### settings/database.py
This file SHOULD ONLY contain the variable DATABASES, which is of course
where you configure the database!

Initially this file is configured with a SQLite database relative to the root
of the project.

** This file MUST not be commited or in any way bundled along with the project! **

When deploying the project into a new environment you should simply reconfigure
a new database.py file from the database.py.template file.

### settings/{development,local,staging,testing,production}.py
By default the development.py settings file is used, however
if a local.py file is found then that takes preference instead.

The development settings should work for most new developers on
the project, however if you need to introduce new settings before release
or to adjust for any changes the environment might have introduced
this is the file to use!

Simply copy development.py to local.py and get hacking!

The local.py MUST NOT be commited or bundled in any way with the project!
This is local to the developer only!

## Features
* Requirements specification splitted into environment specifics
* Settings splitted into environment environment specifics
* Automatically generated SECRET_KEY

## Enabled applications
* [django-apptemplates](https://pypi.python.org/pypi/django-apptemplates/)
* [South](https://pypi.python.org/pypi/South)
* [django-annoying](https://pypi.python.org/pypi/django-annoying)
* [django-extensions](https://pypi.python.org/pypi/django-extensions)
* [django-debug-toolbar](https://pypi.python.org/pypi/django-debug-toolbar)

=========
TicTASCII
=========

Synergetically revolutionalizing mobile Tic Tac Toe in the cloud.

Prerequisites
=============

To run this project, you will need the following:

* A Linux system.
* Python 2.7.
* ``make``
* ``pip`` (optional, but recommended)
* ``virtualenv`` (optional, but recommended)

Quick start
===========

For a system-wide installation::

    $ easy_install tictascii   # install (as root, unless in a virtualenv)
    $ ticli.py                 # run

Installation
============

You can install the latest released version of the package by running
``easy_install tictascii`` or ``pip install tictascii``.

We recommend installing the package within a virtualenv, in order to
install the project using virtualenv, you'll have to create an environment
with the ``virtualenv`` command::

    $ cd ~/virtualenvs  # any directory will do
    $ virtualenv tictascii  # create a virtual environment
    $ . tictascii/bin/activate  # activate virtual environment
    (tictascii)$ pip install tictascii  # install package into the environment

Packages inside this environment do not require you to install any packages
into the system-level Python instance.  As a corollary, you won't have to run
``sudo`` to assume root privileges at any point when working with this project.

Running
=======

After you've installed the package, ``ticli.py`` can be executed from any
directory as long as your Python is installed correctly (specifically,
your Python's ``bin/`` folder must be in the path).

Developing
==========

To develop for this project, you'll need to be aware of the development tools
and processes use to create cutting-edge Tic Tac Toe features.

Additional prerequisites
~~~~~~~~~~~~~~~~~~~~~~~~

In addition to the regular prerequisites for users, you will need a recent
version of `git`.

Commit access
~~~~~~~~~~~~~

Only those who have write access to the repository can commit code.  Others
who want to contribute code can submit their patches using the GitHub
"Pull Requests" mechanism.

Checking out the code
~~~~~~~~~~~~~~~~~~~~~

To check out the code, clone the ``https://github.com/enginous/tictascii.git``
git repository.  In a Linux shell, you can do this like so::

    $ git clone https://github.com/enginous/tictascii.git

Installing required packages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can install the required packages by running the following command::

    $ make install

We recommend running this within a virtual environment, as described in
`Installation`_.  Otherwise, you will have to run this command as root.

Running tests
~~~~~~~~~~~~~

Tests are considered to be successful if all of the following critera are met:

* All Python tests (as found by the ``nose`` module) run without errors or
  failures.
* Code is PEP-8 compliant (as determined by the ``pep8`` module).

Building
~~~~~~~~

To create an installable ZIP bundle from the source, run ``make build``. This
will run all the tests and proceed to create a ``.zip`` in the directory
``tictascii-dist`` that resides as a sibling to the working directory,
``tictascii``.  From within the working directory, run::

    $ make build

You can then unbundle the zip to view the source code, or install it using
the following command (given version 0.0.2 as specified in ``setup.py``)::

    $ easy_install ../tictascii-dist/tictascii-0.0.2.zip

Automatic continuous integration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://secure.travis-ci.org/enginous/tictascii.png?branch=master

Builds are run using Travis.  Every time a commit is made into the repository,
Travis runs the ``make test`` command to ensure that the build passes.

You can view past builds in the system at the `build system page`_.

.. _`build system page`: https://travis-ci.org/enginous/tictascii

The life of a TicTASCII developer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After retrieving the project, developers should work in iterations similar
to the following:

0.  (Preferably create a feature branch and a corresponding pull request
    when changes have been made.)
1.  Run ``make test``.
2.  Add failing test.
3.  Run tests to verify that the test fails.
4.  Add functionality fixing failing test.
5.  Run tests to verify that functionality fixes test.
6.  Repeat steps 2-4 as many times as you need to create a logical change
    that warrants committing.
7.  Commit changes.
8.  Push when you have accrued enough changes to add enough functionality
    to the project that users can benefit from it.
9.  Ensure that the Travis build succeeds.  Fix if necessary.
10. If you opted for pull requests, asssign to another project member and wait
    until that project member merges your changes.
11. Repeat process for next change.
bash.py
=======

.. image:: https://travis-ci.org/jpetrucciani/bash.py.svg?branch=master
    :target: https://travis-ci.org/jpetrucciani/bash.py


.. image:: https://badge.fury.io/py/bash.py.svg
   :target: https://badge.fury.io/py/bash.py
   :alt: PyPI version


.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/ambv/black
   :alt: Code style: black


.. image:: https://img.shields.io/badge/python-3.6+-blue.svg
   :target: https://www.python.org/downloads/release/python-360/
   :alt: Python 3.6+ supported


An inline Bash script runner, for Python.
-----------------------------------------

Example Usage
~~~~~~~~~~~~~

.. code:: pycon

   >>> import bash

   >>> bash.run("echo hi")
   <BashProcess pid=24108 return_code=0>

   >>> _.output
   'hi\n'

Installation
~~~~~~~~~~~~

.. code:: shell

   $ pipenv install bash.py
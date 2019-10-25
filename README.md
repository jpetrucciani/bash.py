[![image](https://travis-ci.org/jpetrucciani/bash.py.svg?branch=master)](https://travis-ci.org/jpetrucciani/bash.py)
[![PyPI
version](https://badge.fury.io/py/bash.py.svg)](https://badge.fury.io/py/bash.py)
[![Code style:
black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![Python 3.6+
supported](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/release/python-360/)

# An inline Bash script runner, for Python.

## Example Usage

```pycon
>>> import bash

>>> bash.run("echo hi")
<BashProcess pid=24108 return_code=0>

>>> proc = _
>>> proc.output
'hi\n'

>>> proc.return_code
0
```

## Installation

```shell
$ pipenv install bash.py
```

# bash.py
## An inline Bash script runner, for Python.

### Example Usage

```pycon
>>> import bash

>>> bash.run("echo hi")
<BashProcess pid=24108 return_code=0>

>>> _.output
'hi\n'
```

### Installation

```shell
$ pipenv install bash.py
```

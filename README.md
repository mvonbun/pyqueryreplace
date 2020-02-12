# PYQUERYREPLACE
Python 3 module for user-queried search-and-replace.

## Installation

From your local copy
``` shell
git pull https://github.com/mvonbun/pyqueryreplace
cd pyqueryreplace
python3 -m pip install --user query-replace-mvonbun
```

or

``` shell
git pull https://github.com/mvonbun/pyqueryreplace
cd pyqueryreplace
python3 -m pip install --user --upgrade setuptools wheel
python3 setup.py sdist bdist_wheel
```


## Usage
### Module Usage via Import
Import the package, example from `ipyton3`:

``` python
In [1]: qrr_re = pyqueryreplace.pyqrr.Qrr(re.compile(r'\\'), '|')

In [2]: import pyqueryreplace.pyqrr as pyqrr

In [3]: import re

In [4]: qrr_re = pyqueryreplace.pyqrr.Qrr(re.compile(r'\\'), '|')
```

### Command Line Script Usage
You can use `pyqueryreplace` as a command line script:

``` shell
./pyqrr.py --help
usage: pyqrr.py [-h] [--output OUTPUT] [--demo] [--dry] [--bak BAK]
                [regexp] [sub] [input]

positional arguments:
  regexp           regexp to search for
  sub              regexp substitute
  input            input filename to query-search-replace

optional arguments:
  -h, --help       show this help message and exit
  --output OUTPUT  output filename to store result
  --demo           show command line demo and exit
  --dry            dry run (not actually replacing)
  --bak BAK        backup file extension
```


## Dependencies
`pyqueryreplace` uses the packages
- [pygetch](https://github.com/mvonbun/pygetch) to capture uninterrupted user
  input
- [pyprintfancy](https://github.com/mvonbun/pyprintfancy) to show original and
  replacement text

devmine-core
============

Dig into the mine of developers to find precious gems

Contribute
==========

This project uses mainly `python` in version 3.
The easiest way to have every required libraries is to use a virtual
environment:

* install `virtualenv` if necessary
* set up a virtual environment: `virtualenv -p python env` (replace `python`
  with `python3` if `python 3` is not your default `python` version)
* activate it: `source env/bin/activate`
* install the required libraries through `pip`:
  `pip install -r requirements.txt`

When contributing, make sure that your changes are conform to PEP8 by running
`invoke pep8`.

# devmine-core

Dig into the mine of developers to find precious gems.

## Setup

This project uses mainly `python` in version 3.
The easiest way to have every required libraries is to use a virtual
environment:

* Install `virtualenv` if necessary.
* Set up a virtual environment: `virtualenv -p python env` (replace `python`
  with `python3` if `python 3` is not your default `python` version).
* Activate it: `source env/bin/activate`.
* Install the required libraries using `pip`:
  `pip install -r requirements.txt`
* When contributing to the project, you also need to install development
  requirements:
  `pip install -r requirements_dev.txt`
* Install a server backend. This should be corresponding to what you configure
  in the settings. Default is `tornado`:
  `pip install tornado`
* For a basic setup, run the following command:
  `invoke setup`
* If you do not need to tweak anything, simply run the application:
  `python run.py`

When contributing, make sure that your changes are conform to PEP8 by running
`invoke pep8`. You may also want to do a static analysis of the code:
`invoke pyflakes`. To run a full check (both PEP8 and static analysis), run:
`invoke check`

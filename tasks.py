from shutil import copy
import sys
from invoke import (
    task,
    run
)

# define projects directories
tools_dir = 'tools'
devmine_dir = 'devmine'
config_dir = devmine_dir + '/config'
test_dir = devmine_dir + '/test'
func_test_dir = test_dir + '/functional'
unit_test_dir = test_dir + '/unit'


@task
def set_settings(environment='production', nosetests=''):
    if environment not in ['production', 'development', 'test']:
        print('Error: ' + environment + ' is not a valid parameter',
              file=sys.stderr)
        exit(1)

    src = config_dir + '/settings-' + environment + '.py.sample'
    dst = config_dir + '/settings.py'
    print('Copying ' + src + ' to ' + dst)
    copy(src, dst)
    print('Done')


@task('set_settings')
def test_func(environment='test', nosetests='nosetests'):
    run_cmd(nosetests + ' -w ' + func_test_dir)


@task('set_settings')
def test_unit(environment='test', nosetests='nosetests'):
    run_cmd(nosetests + ' -w ' + unit_test_dir)


@task('set_settings', 'test_func', 'test_unit')
def test(environment='test', nosetests='nosetests'):
    pass


@task('set_settings')
def setup():
    src = 'alembic.ini.sample'
    dst = 'alembic.ini'
    print('Copying ' + src + ' to ' + dst)
    copy(src, dst)
    print('Done')


@task
def pep8():
    cmd = 'pep8 run.py tasks.py ' + devmine_dir + ' ' + tools_dir
    run_cmd(cmd)


@task
def pyflakes():
    cmd = 'pyflakes run.py tasks.py ' + pydeo_dir
    run_cmd(cmd)


@task('pep8', 'pyflakes')
def check():
    pass


@task
def clean():
    run_cmd("find . -name '__pycache__' -exec rm -rf {} +")
    run_cmd("find . -name '*.pyc' -exec rm -f {} +")
    run_cmd("find . -name '*.pyo' -exec rm -f {} +")
    run_cmd("find . -name '*~' -exec rm -f {} +")
    run_cmd("find . -name '._*' -exec rm -f {} +")


@task('clean')
def clean_env():
    run_cmd('rm -r ./env && mkdir env && touch env/.keep')


def run_cmd(cmd):
    "Run a system command verbosely."
    print('Running \'' + cmd + '\'...')
    run(cmd)
    print('Done')

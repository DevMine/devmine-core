from invoke import (
    task,
    run
)

# define projects directories
tools_dir = 'tools'


@task
def pep8():
    cmd = 'pep8 tasks.py ' + tools_dir
    run_cmd(cmd)


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

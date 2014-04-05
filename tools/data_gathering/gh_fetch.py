import codecs
import json
import time
from getpass import getpass

from github3 import (
    GitHub,
    GitHubError,
    login
)


import gh_settings as settings


def dump_users(users):
    """Take a list of users as json and dump them to the json file for users as
    defined in settings."""

    fp = codecs.open(settings.USERS_DATASET, 'a', 'utf-8')
    json.dump(users, fp)
    fp.close()


def dump_repos(repos):
    """Take a list of repositories as json and dump them to the json file for
    repositories as defined in settings."""

    fp = codecs.open(settings.REPOS_DATASET, 'a', 'utf-8')
    json.dump(repos, fp)
    fp.close()


def main():
    user = input('GitHub username: ')
    password = getpass('GitHub password: ')

    if user and password:
        gh = login(user, password)
    else:
        gh = GitHub()

    # It is defined inside the main because it makes use of the current gh
    def call_or_wait(function, *args, **kargs):
        '''Given a function and some arguments, tries to execute the function
        or waits until the ratelimit is reset.'''

        success = False
        while not success:
            try:
                result = function(*args, **kargs)
                success = True
            except GitHubError as e:
                if e.code == 403:
                    # rate limit exceeded
                    reset = gh.rate_limit()['rate']['reset']
                    wait_time = int(reset - time.time()) + 1

                    print("Not enough API calls. Waiting for",
                          int(wait_time / 60), "minutes and",
                          wait_time % 60, "seconds")

                    time.sleep(wait_time)
                else:
                    raise e

        return result

    # fetch none random developers
    devmine = call_or_wait(lambda:
                           gh.organization("DevMine").iter_public_members())
    # the lambda is used to make the call lazy, as there are multiple API
    # calls involved in the statement

    devs = [dev.login for dev in devmine]

    # fetch random developers
    for repo in call_or_wait(gh.iter_all_repos, number=3000, since=3452093):
        if repo.private:
            continue
        devs.append(repo.owner)

    print(len(devs), "developers fetched")

    users = []
    repos = []

    # dump developers and their repositories
    for dev in devs:
        u = call_or_wait(gh.user, dev)
        users.append(u.to_json())
        if len(users) % 500 == 0:
            print("Repos feched for", len(users), "developers")
        repos.extend(call_or_wait(gh.iter_user_repos, u.login))

    dump_users(users)
    dump_repos(repos)


if __name__ == "__main__":
    main()

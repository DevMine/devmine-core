import codecs
import json

from github3 import (
    GitHub,
    iter_user_repos,
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
    if settings.GH_USER and settings.GH_PASSWORD:
        gh = login(settings.GH_USER, settings.GH_PASSWORD)
    else:
        gh = GitHub()

    # fetch none random developers
    devs = [user.login for user in
            gh.organization("DevMine").iter_public_members()]

    # fetch random developers
    for repo in gh.iter_all_repos(number=3000, since=3452093):
        if repo.private:
            continue
        devs.append(repo.owner)

    users = []
    repos = []

    # dump developers and their repositories
    for dev in devs:
        u = gh.user(dev)
        users.append(u.to_json())
        for repo in iter_user_repos(u.login):
            repos.append(repo.to_json())

    dump_users(users)
    dump_repos(repos)


if __name__ == "__main__":
    main()

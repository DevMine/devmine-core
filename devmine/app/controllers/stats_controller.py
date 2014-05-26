import json

from bottle import abort
from sqlalchemy import func

from devmine.app.controllers.application_controller import (
    ApplicationController
)
from devmine.app.helpers import application_helper as ah
from devmine.app.models.user import User
from devmine.app.models.github.user import GithubUser


class StatsController(ApplicationController):
    """Class for handling the stats page."""

    __gh_users_count = None
    __users_count = None

    def index(self, db):
        """Render index page."""

        if self.__gh_users_count is None or self.__users_count is None:
            try:
                self.__gh_users_count = db.query(
                    func.count(GithubUser.id)).scalar()
                self.__users_count = db.query(
                    func.count(user.id)).scalar()
            except:
                abort(500, 'Internal server error')

        stats = {
            'users-count': self.__users_count,
            'github-users-count': self.__gh_users_count
        }

        return json.dumps(stats, cls=ah.AlchemyEncoder)

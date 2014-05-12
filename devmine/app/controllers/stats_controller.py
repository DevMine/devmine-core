import json

from bottle import abort
from sqlalchemy import func

from devmine.app.controllers.application_controller import (
    ApplicationController
)
from devmine.app.helpers import application_helper as ah
from devmine.app.models.developer import Developer
from devmine.app.models.user import User


class StatsController(ApplicationController):
    """Class for handling the stats page."""

    __users_count = None
    __developers_count = None

    def index(self, db):
        """Render index page."""

        if self.__users_count is None or self.__developers_count is None:
            try:
                self.__users_count = db.query(func.count(User.id)).scalar()
                self.__developers_count = db.query(
                    func.count(Developer.id)).scalar()
            except:
                abort(500, 'Internal server error')

        stats = {
            'developers-count': self.__developers_count,
            'users-count': self.__users_count
        }

        return json.dumps(stats, cls=ah.AlchemyEncoder)

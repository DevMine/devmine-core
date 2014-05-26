import json

from sqlalchemy.orm.exc import NoResultFound

from devmine.app.models.github.user import GithubUser
from devmine.app.controllers.application_controller import (
    ApplicationController
)
from devmine.app.helpers import application_helper as ah


class GithubUsersController(ApplicationController):

    def index(self, db):
        """Return the list of all users."""
        since_id = super().get_since_id()
        try:
            users = db.query(GithubUser).filter(
                GithubUser.id >= since_id).limit(100).all()
        except NoResultFound:
            users = {}
        return json.dumps(users, cls=ah.AlchemyEncoder)

    def show(self, db, id):
        """Return the user corresponding to the given id."""
        super().assert_id(id)
        try:
            user = db.query(GithubUser).filter_by(id=id).one()
        except NoResultFound:
            user = {}
        return json.dumps(user, cls=ah.AlchemyEncoder)

    def login(self, db, login):
        """Return the user corresponding to the given login."""
        try:
            login = db.query(GithubUser).filter_by(login=login).all()
        except NoResultFound:
            login = {}
        return json.dumps(login, cls=ah.AlchemyEncoder)

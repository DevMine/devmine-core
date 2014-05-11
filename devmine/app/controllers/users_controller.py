import json

from sqlalchemy.orm.exc import NoResultFound

from devmine.app.models.user import User
from devmine.app.controllers.application_controller import (
    ApplicationController
)
from devmine.app.helpers import application_helper as ah


class UsersController(ApplicationController):

    def index(self, db):
        """Return the list of all users."""
        return json.dumps(db.query(User).all(), cls=ah.AlchemyEncoder)

    def show(self, db, id):
        """Return the user corresponding to the given id."""
        try:
            user = db.query(User).filter_by(id=id).one()
        except NoResultFound:
            user = {}
        return json.dumps(user, cls=ah.AlchemyEncoder)

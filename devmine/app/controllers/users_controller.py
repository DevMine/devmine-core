import json

from bottle import request
from sqlalchemy.orm.exc import NoResultFound

from devmine.app.models.user import User
from devmine.app.controllers.application_controller import (
    ApplicationController
)
from devmine.app.helpers import application_helper as ah


class UsersController(ApplicationController):

    def index(self, db):
        """Return the list of all users."""
        if 'since' in request.query:
            since_id = int(request.query['since'])
        else:
            since_id = 0
        try:
            users = db.query(User).filter(User.id.between(
                since_id, since_id + 100)).all()
        except NoResultFound:
            users = {}
        return json.dumps(users, cls=ah.AlchemyEncoder)

    def show(self, db, id):
        """Return the user corresponding to the given id."""
        try:
            user = db.query(User).filter_by(id=id).one()
        except NoResultFound:
            user = {}
        return json.dumps(user, cls=ah.AlchemyEncoder)

import json

from devmine.app.models.user import User
from devmine.app.controllers.application_controller import (
    ApplicationController
)
from devmine.app.helpers import application_helper as ah


class UsersController(ApplicationController):

    def index(self, db):
        return json.dumps(db.query(User).all(), cls=ah.AlchemyEncoder)

import json

from devmine.app.models.developer import Developer
from devmine.app.controllers.application_controller import (
    ApplicationController
)
from devmine.app.helpers import application_helper as ah


class DevelopersController(ApplicationController):

    def index(self, db):
        return json.dumps(db.query(Developer).all(), cls=ah.AlchemyEncoder)

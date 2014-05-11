import json

from devmine.app.models.repository import Repository
from devmine.app.controllers.application_controller import (
    ApplicationController
)
from devmine.app.helpers import application_helper as ah


class RepositoriesController(ApplicationController):

    def index(self, db):
        return json.dumps(db.query(Repository).all(), cls=ah.AlchemyEncoder)

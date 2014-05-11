import json

from devmine.app.models.score import Score
from devmine.app.controllers.application_controller import (
    ApplicationController
)
from devmine.app.helpers import application_helper as ah


class ScoresController(ApplicationController):

    def index(self, db):
        return json.dumps(db.query(Score).all(), cls=ah.AlchemyEncoder)

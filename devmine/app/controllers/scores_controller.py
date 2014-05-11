import json

from sqlalchemy.orm.exc import NoResultFound

from devmine.app.models.score import Score
from devmine.app.controllers.application_controller import (
    ApplicationController
)
from devmine.app.helpers import application_helper as ah


class ScoresController(ApplicationController):

    def index(self, db):
        """Return the list of all scores."""
        return json.dumps(db.query(Score).all(), cls=ah.AlchemyEncoder)

    def show(self, db, id):
        """Return the repository corresponding to the given id."""
        try:
            score = db.query(Score).filter_by(id=id).one()
        except NoResultFound:
            score = {}
        return json.dumps(score, cls=ah.AlchemyEncoder)

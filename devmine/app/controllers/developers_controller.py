import json

from sqlalchemy.orm.exc import NoResultFound

from devmine.app.models.developer import Developer
from devmine.app.controllers.application_controller import (
    ApplicationController
)
from devmine.app.helpers import application_helper as ah


class DevelopersController(ApplicationController):

    def index(self, db):
        """Return the list of all developers."""
        return json.dumps(db.query(Developer).all(), cls=ah.AlchemyEncoder)

    def show(self, db, id):
        """Return the developer correspond to the given id."""
        try:
            developer = db.query(Developer).filter_by(id=id).one()
        except NoResultFound:
            developer = {}
        return json.dumps(developer, cls=ah.AlchemyEncoder)

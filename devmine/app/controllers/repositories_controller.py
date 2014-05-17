import json

from bottle import abort
from sqlalchemy.orm.exc import NoResultFound

from devmine.app.models.repository import Repository
from devmine.app.controllers.application_controller import (
    ApplicationController
)
from devmine.app.helpers import application_helper as ah


class RepositoriesController(ApplicationController):

    def index(self, db):
        """Return the list of all repositories."""
        since_id = super().get_since_id()
        try:
            repositories = db.query(Repository).filter(
                Repository.id >= since_id).limit(100).all()
        except NoResultFound:
            repositories = {}
        return json.dumps(repositories, cls=ah.AlchemyEncoder)

    def show(self, db, id):
        """Return the repository corresponding to the given id."""
        try:
            int(id)
        except:
            abort(400, 'invalid id')

        try:
            repository = db.query(Repository).filter_by(id=id).one()
        except NoResultFound:
            repository = {}
        return json.dumps(repository, cls=ah.AlchemyEncoder)

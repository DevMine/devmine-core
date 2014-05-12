import json

from sqlalchemy.orm.exc import NoResultFound

from devmine.app.models.feature import Feature
from devmine.app.controllers.application_controller import (
    ApplicationController,
    enable_cors
)
from devmine.app.helpers import application_helper as ah


class FeaturesController(ApplicationController):
    """Class for handling requests on the feature resource."""

    def index(self, db):
        since_id = super().get_since_id()
        try:
            features = db.query(Feature).filter(
                Feature.id >= since_id).limit(100).all()
        except NoResultFound:
            features = {}
        return json.dumps(features, cls=ah.AlchemyEncoder)

    def by_category(self, db):
        """Return all features sorted by category as a JSON string
        like the following:
            {'category1': ['feature1': {...}, ...], 'category2': [...]}
        """

        enable_cors()

        features = db.query(Feature).order_by(
            Feature.category, Feature.name).all()

        if len(features) == 0:
            return ""

        retval = {}
        for f in features:
            if f.category not in retval:
                retval[f.category] = []
            retval[f.category].append(ah.obj_to_json(f))

        return json.dumps(retval)

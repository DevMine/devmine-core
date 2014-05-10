import json
import logging
from io import StringIO
from urllib import parse

from bottle import abort
from devmine.lib.composition import construct_weight_vector
from devmine.app.controllers.application_controller import (
    ApplicationController
)


class SearchController(ApplicationController):
    """Class for handling search query."""

    def query(self, db, q):
        """Return search result as a JSON string"""
        try:
            io = StringIO(parse.unquote(q))
            feature_weights = json.load(io)
            construct_weight_vector(db, feature_weights)
        except:
            logging.exception('SearchController:query')
            abort(400, 'Malformed JSON query')

        # TODO send the feature weights to the composition function
        # and send back the result as a JSON string.
        return json.dumps("TODO")

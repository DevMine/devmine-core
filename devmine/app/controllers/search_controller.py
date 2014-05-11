import json
import logging
from io import StringIO
from urllib import parse

from bottle import abort
from devmine.lib.composition import rank
from devmine.app.controllers.application_controller import (
    ApplicationController
)


class SearchController(ApplicationController):
    """Class for handling search query."""

    def query(self, db, q):
        """Return search result as a JSON string"""

        enable_cors()

        try:
            io = StringIO(parse.unquote(q))
            feature_weights = json.load(io)
            ranking = rank(db, feature_weights)
        except:
            logging.exception('SearchController:query')
            abort(400, 'Malformed JSON query')
        return json.dumps(ranking)

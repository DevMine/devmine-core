import json
from io import StringIO
from bottle import abort
from devmine.app.controllers.application_controller import (
    ApplicationController
)


class SearchController(ApplicationController):
    """Class for handling search query."""

    def query(self, q):
        """Return search result as a JSON string"""
        io = StringIO(q)
        try:
            feature_weights = json.load(io)
        except:
            abort(400, 'Malformed JSON query')

        # TODO send the feature weights to the composition function
        # and send back the result as a JSON string.
        return json.dumps("TODO")

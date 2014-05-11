import json
import logging
from io import StringIO
from urllib import parse

from bottle import abort
from devmine.lib.composition import rank
from devmine.app.controllers.application_controller import (
    ApplicationController,
    enable_cors
)


class SearchController(ApplicationController):
    """Class for handling search query."""

    def query(self, db, q):
        """Return search result as a JSON string"""

        enable_cors()

        try:
            io = StringIO(parse.unquote(q))
            feature_weights = json.load(io)
            ranking, elsapsed_time = rank(db, feature_weights)
        except:
            logging.exception('SearchController:query')
            abort(400, 'Malformed JSON query')


        sorted_ranking = sorted(ranking, key=lambda user: user['rank'],
                reverse=True)
        results = {'results': sorted_ranking,
                   'elapsed_time': "%0.9f" % (elsapsed_time)}

        return json.dumps(results)

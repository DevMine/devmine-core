from bottle import (
    request,
    response
)


class ApplicationController:

    def initialize(self):
        pass

    def get_since_id(self):
        """
        Get <id> passed as a query parameter for queries of this form:
            ?since=42
        The id returned is 0 in case the since parameter is not specified.
        """
        if 'since' in request.query:
            since_id = int(request.query['since'])
        else:
            since_id = 0
        return since_id


def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET'
    response.headers['Access-Control-Allow-Headers'] =\
        'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

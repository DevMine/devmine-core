from bottle import (
    abort,
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
        This method aborts with http error 400 if given id is invalid.
        """
        if 'since' in request.query:
            since_id = request.query['since']
        else:
            since_id = 0
        self.assert_id(since_id)

        return since_id

    def assert_id(self, id):
        """
        Check that <id> is an integer and aborts with http error 400 if it is
        not the case.
        """
        try:
            int(id)
        except:
            abort(400, 'invalid id')


def enable_cors():
    """
    Enable cross-origin resource sharing (CORS) when called from a controller.
    """
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET'
    response.headers['Access-Control-Allow-Headers'] =\
        'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

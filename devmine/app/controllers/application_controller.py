from bottle import response


class ApplicationController:

    def initialize(self):
        pass

    @staticmethod
    def enable_cors(fn):
        """Create decorator to enable Cross-Origin Resource Sharing (CORS)."""
        def _enable_cors(* args, **kwargs):
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Methods'] = 'GET'
            response.headers['Access-Control-Allow-Headers'] =\
                'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
            return fn(*args, **kwargs)

        return _enable_cors

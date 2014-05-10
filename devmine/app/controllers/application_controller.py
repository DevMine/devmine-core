from bottle import response


class ApplicationController:

    def initialize(self):
        pass


def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET'
    response.headers['Access-Control-Allow-Headers'] =\
        'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

from devmine.app.controllers.index_controller import IndexController


def setup_routing(app):
    app.route('/', 'GET', IndexController().index)

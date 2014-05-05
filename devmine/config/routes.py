from devmine.app.controllers.index_controller import IndexController
from devmine.app.controllers.search_controller import SearchController


def setup_routing(app):
    app.route('/', 'GET', IndexController().index)
    app.route('/search/<q>', 'GET', SearchController().query)

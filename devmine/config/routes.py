from devmine.app.controllers.index_controller import IndexController
from devmine.app.controllers.search_controller import SearchController
from devmine.app.controllers.features_controller import FeaturesController


def setup_routing(app):
    app.route('/', 'GET', IndexController().index)
    app.route('/search/<q>', 'GET', SearchController().query)
    app.route('/features/by_category/<category>', 'GET',
              FeaturesController().by_category)

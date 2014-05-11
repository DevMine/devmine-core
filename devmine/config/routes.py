from devmine.app.controllers.assets_controller import AssetsController
from devmine.app.controllers.index_controller import IndexController
from devmine.app.controllers.search_controller import SearchController
from devmine.app.controllers.users_controller import UsersController
from devmine.app.controllers.features_controller import FeaturesController


def setup_routing(app):
    app.route('/favicon.ico', 'GET', AssetsController.favicon)
    app.route('/favicon.png', 'GET', AssetsController.favicon)

    app.route('/', 'GET', IndexController().index)
    app.route('/search/<q>', 'GET', SearchController().query)
    app.route('/features/by_category', 'GET',
              FeaturesController().by_category)
    app.route('/users', 'GET', UsersController().index)

from devmine.app.controllers.assets_controller import AssetsController
from devmine.app.controllers.developers_controller import DevelopersController
from devmine.app.controllers.features_controller import FeaturesController
from devmine.app.controllers.index_controller import IndexController
from devmine.app.controllers.users_controller import UsersController
from devmine.app.controllers.repositories_controller import (
    RepositoriesController
)
from devmine.app.controllers.scores_controller import ScoresController
from devmine.app.controllers.search_controller import SearchController


def setup_routing(app):
    # static assets
    app.route('/favicon.ico', 'GET', AssetsController.favicon)
    app.route('/favicon.png', 'GET', AssetsController.favicon)

    # default route
    app.route('/', 'GET', IndexController().index)

    # developers
    app.route('/developers', 'GET', DevelopersController().index)
    app.route('/developers/<id>', 'GET', DevelopersController().show)

    # features
    app.route('/features', 'GET', FeaturesController().index)
    app.route('/features/by_category', 'GET', FeaturesController().by_category)

    # repositories
    app.route('/repositories', 'GET', RepositoriesController().index)

    # scores
    app.route('/scores', 'GET', ScoresController().index)

    # search
    app.route('/search/<q>', 'GET', SearchController().query)

    # users
    app.route('/users', 'GET', UsersController().index)
    app.route('/users/<id>', 'GET', UsersController().show)

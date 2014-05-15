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
from devmine.app.controllers.stats_controller import StatsController


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
    app.route('/repositories/<id>', 'GET', RepositoriesController().show)

    # scores
    app.route('/scores', 'GET', ScoresController().index)
    app.route('/scores/<id>', 'GET', ScoresController().show)

    # search
    app.route('/search/<q>', 'GET', SearchController().query)

    # stats
    app.route('/stats', 'GET', StatsController().index)

    # users
    app.route('/users', 'GET', UsersController().index)
    app.route('/users/<id>', 'GET', UsersController().show)
    app.route('/users/login/<login>', 'GET', UsersController().login)

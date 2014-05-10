from bottle import static_file

from devmine.app.controllers.application_controller import (
    ApplicationController
)


class AssetsController(ApplicationController):
    """Controller that handles static assets."""

    def favicon():
        return static_file('favicon.ico', root='devmine/app/assets/img')

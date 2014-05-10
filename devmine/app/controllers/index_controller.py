import json

import devmine
from devmine.app.controllers.application_controller import (
    ApplicationController
)


class IndexController(ApplicationController):
    """Class for handling index page."""

    def index(self):
        """Render index page."""
        data = {
            "devmine-version:": devmine.Devmine.get_version(),
            "api-version:": devmine.Devmine.get_api_version()
        }
        return json.dumps(data)

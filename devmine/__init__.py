__devmine_version__ = '0.1.0'
__api_version__ = '1'

import logging

import bottle
from bottle.ext import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from devmine.app.models import Base
from devmine.config import routes
from devmine.lib import composition


class Devmine:

    def __init__(self,
                 server='auto',
                 host='0.0.0.0',
                 port=8080,
                 db_url='sqlite:///:memory:',
                 db_echo=False,
                 reloader=False,
                 debug=False):
        self.server_type = server
        self.host = host
        self.port = port
        self.reloader = reloader
        self.debug = debug

        self.api_version = __api_version__
        self.devmine_version = __devmine_version__

        self.app = bottle.Bottle()

        routes.setup_routing(self.app)

        bottle.debug(self.debug)

        engine = create_engine(db_url, echo=db_echo)

        sqlalchemy_plugin = sqlalchemy.Plugin(
            engine,
            Base.metadata,
            keyword='db',
            create=True,
            commit=True,
            use_kwargs=False
        )
        self.app.install(sqlalchemy_plugin)

        create_session = sessionmaker(bind=engine)
        session = create_session()
        logging.info('Prefetching the scores matrix...')
        composition.get_scores_matrix(session)
        session.close()

    @staticmethod
    def get_version():
        """Return devmine version."""
        return __devmine_version__

    @staticmethod
    def get_api_version():
        """Return devmine API version."""
        return __api_version__

#!/usr/bin/env python
# coding: utf-8

import bottle
from logging import info

from devmine import Devmine
from devmine.config import (
    environment,
    settings
)


def main():
    info('Devmine server started')
    db_url = settings.db_url
    server = settings.server
    if not db_url:
        db_url = environment.db_url
    if not server:
        server = environment.server

    info('\nServer settings:\n'
         'server = %s\n'
         'host = %s\n'
         'port = %s\n'
         'db_url = %s\n'
         'db_echo = %s\n'
         'reloader = %s\n'
         'debug = %s\n',
         server,
         settings.host,
         settings.port,
         db_url,
         environment.db_echo,
         environment.reloader,
         environment.debug)

    a = Devmine(
        server=server,
        host=settings.host,
        port=settings.port,
        db_url=db_url,
        db_echo=environment.db_echo,
        reloader=environment.reloader,
        debug=environment.debug
    )

    bottle.run(
        a.app,
        server=a.server_type,
        reloader=a.reloader,
        host=a.host,
        port=a.port
    )

if __name__ == "__main__":
    main()

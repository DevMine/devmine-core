import os

from devmine.config import settings

if settings.environment == 'production':
    import devmine.config.environments.production as env
elif settings.environment == 'development':
    import devmine.config.environments.development as env
elif settings.environment == 'test':
    import devmine.config.environments.test as env
else:
    raise RuntimeError("Environment not set or incorrect")

server = env.server
debug = env.debug
reloader = env.reloader
db_url = env.db_url
db_echo = env.db_echo

from sqlalchemy import (
    Column,
    Integer,
    String
)

from devmine.app.models import Base


class User(Base):
    """Model of a user."""

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    nickname = Column(String)
    realname = Column(String)

    def __init__(self):
        self.nickname = ''
        self.realname = ''

from sqlalchemy import (
    Column,
    Integer,
    String
)

from devmine.app.models import Base


class Developer(Base):
    """Model of a developer."""

    __tablename__ = 'developers'

    id = Column(Integer, primary_key=True)
    nickname = Column(String)
    name = Column(String)
    location = Column(String)
    email = Column(String)
    blog = Column(String)

    def __init__(self):
        self.nickname = ''
        self.name = ''
        self.location = ''
        self.email = ''
        self.blog = ''

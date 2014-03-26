from sqlalchemy import (
    Column,
    Integer,
    String
)

from devmine.app.models import Base


class Repository(Base):
    """Model of a source code repository."""

    __tablename__ = 'repositories'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    homepage = Column(String)

    def __init__(self):
        self.name = ''
        self.description = ''
        self.homepage = ''

from sqlalchemy import (
    Column,
    Integer,
    String
)

from devmine.app.models import Base


class Feature(Base):
    """Model of a feature."""

    __tablename__ = 'features'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    category = Column(String, nullable=False)

    def __init__(self):
        pass

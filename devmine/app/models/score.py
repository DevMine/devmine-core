from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    String,
    Float
)

from devmine.app.models import Base


class Score(Base):
    """Model of a score."""

    __tablename__ = 'scores'

    id = Column(Integer, primary_key=True)
    uid = Column(Integer,
                 ForeignKey('users.id'),
                 nullable=False)
    fname = Column(String,
                   ForeignKey('features.name'),
                   nullable=False)
    score = Column(Float)

    def __init__(self):
        pass

from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    String
)

from devmine.app.models import Base


class Score(Base):
    """Model of a score."""

    __tablename__ = 'scores'

    id = Column(Integer, primary_key=True)
    ulogin = Column(String,
                    ForeignKey('users.login'),
                    nullable=False)
    fname = Column(String,
                   ForeignKey('features.name'),
                   nullable=False)

    def __init__(self):
        pass

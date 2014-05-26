from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text
)

from devmine.app.models import Base


class GithubUser(Base):
    """Model of a gihub user."""

    __tablename__ = 'gh_users'

    id = Column(Integer,
                primary_key=True)
    uid = Column(Integer,
                 ForeignKey('users.id'),
                 nullable=False)
    login = Column(String,
                   nullable=False,
                   unique=True)
    bio = Column(Text)
    blog = Column(String)
    company = Column(String)
    email = Column(String)
    hireable = Column(Boolean)
    location = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __init__(self):
        pass

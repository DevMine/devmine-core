from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Integer,
    String
)

from devmine.app.models import Base


class GithubRepository(Base):
    """Model of a source code repository for a GitHub user."""

    __tablename__ = 'gh_repositories'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    full_name = Column(String)
    description = Column(String)
    homepage = Column(String)
    fork = Column(Boolean)
    language = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __init__(self):
        pass

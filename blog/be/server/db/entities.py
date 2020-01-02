from sqlalchemy.schema import Column
from sqlalchemy.types import Text, BigInteger, DateTime, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Article(Base):

    id = Column(BigInteger, primary_key=True)

    title = Column(Text)
    content = Column(Text)
    body = Column(Text)
    created_at = Column(DateTime)
    popularity_level = Column(Text)

    is_published = Column(Boolean)
    published_at = Column(DateTime)

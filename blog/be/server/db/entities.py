from datetime import datetime

from sqlalchemy.schema import Column

from .setup import db


class Article(db.Model):
    id = Column(db.Integer, primary_key=True, autoincrement=True)

    title = Column(db.Text)
    content = Column(db.Text)
    created_at = Column(db.DateTime, default=datetime.now())
    popularity_level = Column(db.Text, default=None)

    is_published = Column(db.Boolean, default=False)
    published_at = Column(db.DateTime)

    def __init__(self, **kwargs):
        super(Article, self).__init__(**kwargs)

    def __repr__(self):
        return f'<Article {self.id}, title={self.title}, is_published={self.is_published}>'

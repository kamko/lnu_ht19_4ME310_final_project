from server.db import Article
from .marshmallow import ma


class ArticleSchema(ma.ModelSchema):
    class Meta:
        model = Article

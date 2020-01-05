from server.db import Article
from .marshmallow import ma


def _camelcase(s):
    parts = iter(s.split("_"))
    return next(parts) + "".join(i.title() for i in parts)


class ArticleSchema(ma.ModelSchema):
    class Meta:
        model = Article

    def on_bind_field(self, field_name, field_obj):
        field_obj.data_key = _camelcase(field_obj.data_key or field_name)

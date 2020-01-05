from flask import Blueprint, request

from server import AppConfiguration
from server.db import Article
from server.serialization import ArticleSchema
from server.views.util import jsonify_page

blueprint = Blueprint('article', __name__)

_article_schema = ArticleSchema(exclude=['popularity_level', 'created_at', 'is_published'])
_articles_schema = ArticleSchema(exclude=['popularity_level', 'created_at', 'is_published'], many=True)


@blueprint.route('/<article_id>', methods=['GET'])
def fetch(article_id):
    article = Article.query \
        .filter_by(id=article_id, is_published=True) \
        .first_or_404(article_id)

    return _article_schema.jsonify(article)


@blueprint.route('/', methods=['GET'])
def list_all():
    page_num = request.args.get('page', 1, type=int)
    page = Article.query \
        .filter_by(is_published=True) \
        .order_by(Article.published_at.desc()) \
        .paginate(page_num, AppConfiguration.ITEMS_PER_PAGE, False)

    return jsonify_page(items=_articles_schema.dump(page.items),
                        page=page)

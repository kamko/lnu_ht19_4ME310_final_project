from datetime import datetime

from flask import Blueprint, request

from server.config import AppConfiguration
from server.db import db, Article
from server.serialization import ArticleSchema
from server.views.util import jsonify_page

blueprint = Blueprint('admin', __name__)

_article_schema = ArticleSchema()
_articles_schema = ArticleSchema(many=True)


@blueprint.route('/article', methods=['GET'])
def list_all():
    page_num = request.args.get('page', 1, type=int)
    page = Article.query \
        .order_by(Article.published_at.desc()) \
        .paginate(page_num, AppConfiguration.ITEMS_PER_PAGE, False)

    return jsonify_page(items=_articles_schema.dump(page.items),
                        page=page)


@blueprint.route('/article/<int:article_id>', methods=['GET'])
def fetch(article_id):
    article = Article.query \
        .get_or_404(article_id)

    print(article_id)
    print(article)

    return _article_schema.jsonify(article)


@blueprint.route('/article', methods=['POST'])
# @admin_api_access
def create_article():
    body = request.json
    article = Article(
        title=body['title'],
        content=body['content']
    )

    db.session.add(article)
    db.session.commit()

    return _article_schema.jsonify(article)


@blueprint.route('/article/<int:article_id>', methods=['PUT'])
def update_article(article_id):
    body = request.json

    article = Article.query.get_or_404(article_id)
    article.title = body['title']
    article.content = body['content']

    db.session.add(article)
    db.session.commit()

    return _article_schema.jsonify(article)


@blueprint.route('/article/<int:article_id>/publish', methods=['PUT'])
# @admin_api_access
def publish(article_id):
    article = Article.query.get_or_404(article_id)

    article.is_published = True
    article.published_at = datetime.now()

    db.session.commit()

    return _article_schema.jsonify(article)


@blueprint.route('/article/<int:article_id>/unpublish', methods=['PUT'])
# @admin_api_access
def unpublish(article_id):
    article = Article.query.get_or_404(article_id)

    article.is_published = False
    article.published_at = None

    db.session.commit()

    return _article_schema.jsonify(article)

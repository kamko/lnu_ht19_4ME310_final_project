from datetime import datetime

from flask import Blueprint, request

from server.db import db, Article
from server.serialization import ArticleSchema
from server.views.util import admin_api_access

blueprint = Blueprint('admin', __name__)

_article_schema = ArticleSchema()


@blueprint.route('/article', methods=['POST'])
@admin_api_access
def create_article():
    body = request.json
    article = Article(
        title=body['title'],
        content=body['content']
    )

    db.session.add(article)
    db.session.commit()

    return _article_schema.jsonify(article)


@blueprint.route('/article/<int:article_id>/publish', methods=['PUT'])
@admin_api_access
def publish(article_id):
    article = Article.query.get_or_404(article_id)

    article.is_published = True
    article.published_at = datetime.now()

    db.session.commit()

    return _article_schema.jsonify(article)


@blueprint.route('/article/<int:article_id>/unpublish', methods=['PUT'])
@admin_api_access
def unpublish(article_id):
    article = Article.query.get_or_404(article_id)

    article.is_published = False
    article.published_at = None

    db.session.commit()

    return _article_schema.jsonify(article)

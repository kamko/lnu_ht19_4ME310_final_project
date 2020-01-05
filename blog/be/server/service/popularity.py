from datetime import datetime

from server import db
from server.db import Article


def check_new_articles(app):
    print(datetime.now())

    with app.app_context():
        articles = Article.query \
            .filter_by(popularity_level=None) \
            .all()

        if articles is None or len(articles) == 0:
            print(f'all articles have predictions - skipping run')
            return

        print(f'found {len(articles)} articles without predictions')
        for a in articles:
            _handle(a)


def _handle(article):
    print(f'fetching prediction for article.id={article.id}')
    prediction = _fetch_prediction(article)
    print(f'prediction is {prediction}')

    article.popularity_level = prediction
    db.session.commit()


def _fetch_prediction(article):
    return 3

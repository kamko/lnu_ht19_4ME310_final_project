import functools
from datetime import datetime

import requests

from server import db
from server.config import AppConfiguration
from server.db import Article

print = functools.partial(print, flush=True)


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
    res = requests.post(
        url=f'{AppConfiguration.PREDICTOR_URL}/prediction',
        json={
            'title': article.title,
            'body': article.content
        }
    )
    return res.json()['prediction']

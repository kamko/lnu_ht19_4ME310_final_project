import pickle

from contextlib import contextmanager


def create_engine(conf_file, key):
    import json
    from sqlalchemy import create_engine

    with open(conf_file, 'r') as f:
        conf = json.load(f)
        return create_engine(conf[key]['uri'])


def display_all(df):
    import pandas as pd
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        display(df)


@contextmanager
def figsize(plt, x, y):
    try:
        plt.rcParams['figure.figsize'] = (x, y)
        yield
    finally:
        plt.rcParams['figure.figsize'] = (6.4, 4.8)


def load_df(file_name):
    with open(file_name, 'rb') as f:
        return pickle.load(f)


def save_df(df, file_name):
    with open(file_name, 'wb') as f:
        pickle.dump(df, f)


def save_model(model):
    with open('model.pickle', 'wb') as f:
        pickle.dump(model, f)


def read_model():
    with open('model.pickle', 'rb') as f:
        return pickle.load(f)


def normalize(text):
    import unicodedata

    text = text.replace('\r', '')
    text = text.replace('\n', ' ')
    text = unicodedata.normalize('NFKD', text)

    return text


def create_features(df):
    from textblob import TextBlob
    import pandas as pd

    content_length = []
    number_of_words_in_title = []
    number_of_words_in_content = []

    title_sentiment_polarity = []
    title_sentiment_subjectivity = []

    content_sentiment_polarity = []
    content_sentiment_subjectivity = []

    for row in df.itertuples(index=True):
        title_blob = TextBlob(normalize(row.title))
        body_blob = TextBlob(normalize(row.body))

        content_length.append(len(body_blob))
        number_of_words_in_title.append(len(title_blob.words))
        number_of_words_in_content.append(len(body_blob.words))

        title_sentiment_polarity.append(title_blob.sentiment[0])
        title_sentiment_subjectivity.append(title_blob.sentiment[1])

        content_sentiment_polarity.append(body_blob.sentiment[1])
        content_sentiment_subjectivity.append(body_blob.sentiment[1])

    ndf = pd.DataFrame()

    ndf['content_length'] = content_length
    ndf['number_of_words_in_title'] = number_of_words_in_title
    ndf['number_of_words_in_content'] = number_of_words_in_content

    ndf['title_sentiment_polarity'] = title_sentiment_polarity
    ndf['title_sentiment_subjectivity'] = title_sentiment_subjectivity

    ndf['content_sentiment_polarity'] = content_sentiment_polarity
    ndf['content_sentiment_subjectivity'] = content_sentiment_subjectivity

    return ndf

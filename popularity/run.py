import pandas as pd
from flask import Flask, request

from common import read_model

app = Flask(__name__)

model = read_model()


@app.route('/prediction', methods=['POST'])
def predict():
    req = request.json
    article = {
        'title': req['title'],
        'body': req['body']
    }

    df = pd.DataFrame(article, index=[1])
    features = make_features(df)

    result = model.predict(features)

    return result[0]


def make_features(df):
    return df


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, use_reloader=False)

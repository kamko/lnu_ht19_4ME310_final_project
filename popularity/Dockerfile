FROM kamko/ml-base

COPY requirements.txt run.py common.py model.pickle ./

RUN pip install -r requirements.txt
RUN python -m textblob.download_corpora

EXPOSE 5000
ENTRYPOINT ["python", "run.py"]

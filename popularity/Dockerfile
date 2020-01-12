FROM kamko/ml-base

RUN pip install -r requirements.txt
RUN python -m textblob.download_corpora

COPY requirements.txt run.py common.py model.pickle ./

EXPOSE 5000
ENTRYPOINT ["python", "run.py"]

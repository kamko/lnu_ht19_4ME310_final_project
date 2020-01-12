FROM kamko/ml-base

COPY requirements.txt ./

RUN pip install -r requirements.txt
RUN python -m textblob.download_corpora

COPY run.py common.py model.pickle ./

EXPOSE 5000
ENTRYPOINT ["python", "run.py"]

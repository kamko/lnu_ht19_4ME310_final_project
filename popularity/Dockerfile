FROM kamko/ml-base

COPY requirements.txt run.py model.pickle ./

RUN pip install -r requirements.txt

EXPOSE 5000
ENTRYPOINT ["python", "run.py"]

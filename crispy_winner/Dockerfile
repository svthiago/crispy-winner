FROM centos/python-36-centos7

USER root

RUN mkdir /code

WORKDIR /code

COPY . /code

RUN pip3 install -r requirements.txt

WORKDIR ./carford_api

EXPOSE 5000

CMD python populate_db.py

CMD gunicorn -b 0.0.0.0:5000 -w 4 app:app --reload
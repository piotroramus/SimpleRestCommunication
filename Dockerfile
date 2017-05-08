FROM jfloff/alpine-python

ADD client.py /client.py
ADD server.py /server.py
ADD requirements.txt /requirements.txt

RUN pip install -r requirements.txt

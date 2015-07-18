FROM centurylink/mysql:latest
MAINTAINER lec00q

RUN apt-get update
RUN apt-get install -y python-dev python-pip python-mysqldb

RUN apt-get install python-pip -y

RUN pip install gunicorn
RUN apt-get install python-gevent -y
ADD . /app
WORKDIR /app
RUN pip install bottle

EXPOSE 8080

CMD ["gunicorn","-b","0.0.0.0:8080","-w","3","-k","gevent","--log-file","-","--log-level","debug","--access-logfile","-","main:app"]

FROM ubuntu:latest
MAINTAINER Rishabh Bhardwaj "bhardwajrishabh76@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
ADD . /flask-app
WORKDIR /flask-app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app3.py"]

FROM ubuntu

RUN apt-get update && apt-get -y install python3 && apt-get -y install python3-pip

ENV FLASK_APP main2.py

ENV FLASK_RUN_HOST 0.0.0.0

WORKDIR /project

COPY . /project

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["flask", "run"]
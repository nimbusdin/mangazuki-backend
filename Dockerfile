# start from base
FROM ubuntu:18.04

# install system-wide deps for python and node
RUN apt-get -yqq update
RUN apt-get -yqq install python3
RUN apt-get -yqq install python3-pip python3-dev curl gnupg

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . ./

COPY ./requirements.txt ./
RUN pip3 install --upgrade pip
RUN pip3 install -r ./requirements.txt

RUN black ./application.py

# ENV MODULE_NAME=main
# ENV VARIABLE_NAME=api

EXPOSE 5000

CMD ["python3", "application.py"]

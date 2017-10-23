FROM python:3

WORKDIR /usr/src/app


RUN apt-get update
RUN apt-get install -y python-enchant
RUN apt-get clean
COPY ./ ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -e ./tools


CMD [ "bash" ]

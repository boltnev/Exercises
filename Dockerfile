FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN apt-get update
RUN apt-get install python-enchant
RUN apt-get clean
RUN pip install --no-cache-dir -r requirements.txt

COPY . .:

CMD [ "bash" ]

FROM python:3.6-stretch
WORKDIR /app
COPY . /app
RUN apt-get update
RUN apt-get install build-essential python3-dev -y
RUN pip install -r requirements.txt
RUN chmod +x ./run.sh
ENTRYPOINT ./run.sh

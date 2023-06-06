FROM python:3.8-slim

WORKDIR /app

COPY  ./apps  .

RUN pip install -r ./jobs_microservice/requirements.txt

RUN pip install -r ./api_microservice/requirements.txt

RUN apt update
RUN apt install sqlite3

RUN ["chmod", "+x", "rnscript.sh"]
ENTRYPOINT ["./rnscript.sh"]

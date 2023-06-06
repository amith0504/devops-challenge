FROM python:3.8-slim

WORKDIR /app

COPY  ./apps  .

RUN pip install -r ./jobs_microservice/requirements.txt

RUN pip install -r ./api_microservice/requirements.txt

RUN apt update
RUN apt install sqlite3

RUN ["chmod", "+x", "rnscript.sh"]
ENTRYPOINT ["./rnscript.sh"]
#CMD "python3 ./jobs_microservice/init_db.py" && "python3 ./api_microservice/api.py" && "python3 ./jobs_microservice/jobs.py"
#CMD ["/bin/bash","-c","sleep 15m"]
#CMD ["python3","./api_microservice/api.py"]
#CMD ["python3", "./jobs_microservice/jobs.py"]

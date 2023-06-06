#!/bin/bash
#export JOBS_SERVICE=0.0.0.0
python3 ./jobs_microservice/init_db.py
python3 ./api_microservice/api.py
python3 ./jobs_microservice/jobs.py

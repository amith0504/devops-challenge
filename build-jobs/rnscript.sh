#!/bin/bash
#export JOBS_SERVICE=localhost
python3 ./jobs_microservice/init_db.py
python3 ./jobs_microservice/jobs.py

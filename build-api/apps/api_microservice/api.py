#!/usr/bin/env python
from flask import Flask, request
import requests
import os

app = Flask(__name__)

JOBS_SERVICE = os.environ["JOBS_SERVICE"]  # Please make sure this is defined
print ("jobs service is : ",JOBS_SERVICE)

@app.route("/hello")
def hello():
    return "Hello there"


@app.route("/jobs", methods=["GET"])
def jobs():
    result = requests.get(f"http://173.18.0.5:5001/jobs").content
    return result


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

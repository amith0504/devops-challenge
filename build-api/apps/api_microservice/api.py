#!/usr/bin/env python
from flask import Flask, request
from prometheus_flask_exporter import PrometheusMetrics
import requests
import os

app = Flask(__name__)
metrics = PrometheusMetrics(app)
JOBS_SERVICE = os.environ["JOBS_SERVICE"]  # Please make sure this is defined
print ("jobs service is : ",JOBS_SERVICE)

@app.route("/hello")
@metrics.summary('requests_by_status', 'Request latencies by status',
                 labels={'status': lambda r: r.status_code})
def hello():
    return "Hello there"


@app.route("/jobs", methods=["GET"])
def jobs():
    result = requests.get(f"http://10.96.160.116:5001/jobs").content
    return result


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

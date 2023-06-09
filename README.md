1. First  clone this project 
2. Build the docker images api and jobs devops-challenge/build-api/ and devops-challenge/build-jobs/ respectively .Since I am running in kind I have
   hardcoded the IP in the JOBS_SERVICE environmental variable. 
3. Push the docker images to dockerhub.
4. Run the pulumi up command to deploy the application in kuberenetes application. Pulumi context can be set to use kind (local docker environment) and set the context for namespace in k8s

this two images are pushed to dockerhub and it is pulled by pulumi automatically amith0504/api:15 and amith0504/jobs:1
6. api and jobs service can be accessed both 127.0.0.1:5000/hello and 127.0.0.1:5000/jobs respectively, where jobs service is called from api service internally. 

**API for hello server **

$ curl -vvv 127.0.0.1:5000/hello
*   Trying 127.0.0.1:5000...
* Connected to 127.0.0.1 (127.0.0.1) port 5000 (#0)
> GET /hello HTTP/1.1
> Host: 127.0.0.1:5000
> User-Agent: curl/7.88.1
> Accept: */*
>
< HTTP/1.1 200 OK
< Server: Werkzeug/2.3.5 Python/3.8.17
< Date: Fri, 09 Jun 2023 11:37:14 GMT
< Content-Type: text/html; charset=utf-8
< Content-Length: 11
< Connection: close
<
* Closing connection 0
Hello there

**API for jobs service **

$ curl -vvv 127.0.0.1:5000/jobs
*   Trying 127.0.0.1:5000...
* Connected to 127.0.0.1 (127.0.0.1) port 5000 (#0)
> GET /jobs HTTP/1.1
> Host: 127.0.0.1:5000
> User-Agent: curl/7.88.1
> Accept: */*
>
< HTTP/1.1 200 OK
< Server: Werkzeug/2.3.5 Python/3.8.17
< Date: Fri, 09 Jun 2023 11:37:47 GMT
< Content-Type: text/html; charset=utf-8
< Content-Length: 151
< Connection: close
<
[{"name":"port_scan","status":"Running"},{"name":"content_discovery","status":"Not Running"},{"name":"vulnerability_assessment","status":"Completed"}]
* Closing connection 0

7. Metrics is exposed to the app in 127.0.0.1:5000/metrics after port forwarding the api service in local machine we can access this .

curl -vvv 127.0.0.1:5000/metrics
*   Trying 127.0.0.1:5000...
* Connected to 127.0.0.1 (127.0.0.1) port 5000 (#0)
> GET /metrics HTTP/1.1
> Host: 127.0.0.1:5000
> User-Agent: curl/7.88.1
> Accept: */*
>
< HTTP/1.1 200 OK
< Server: Werkzeug/2.3.5 Python/3.8.17
< Date: Fri, 09 Jun 2023 11:38:39 GMT
< Content-Type: text/plain; version=0.0.4; charset=utf-8
< Content-Length: 6716
< Connection: close
<
# HELP python_gc_objects_collected_total Objects collected during gc
# TYPE python_gc_objects_collected_total counter
python_gc_objects_collected_total{generation="0"} 277.0
python_gc_objects_collected_total{generation="1"} 276.0
python_gc_objects_collected_total{generation="2"} 0.0
# HELP python_gc_objects_uncollectable_total Uncollectable objects found during GC
# TYPE python_gc_objects_uncollectable_total counter
python_gc_objects_uncollectable_total{generation="0"} 0.0
python_gc_objects_uncollectable_total{generation="1"} 0.0
python_gc_objects_uncollectable_total{generation="2"} 0.0
# HELP python_gc_collections_total Number of times this generation was collected
# TYPE python_gc_collections_total counter
python_gc_collections_total{generation="0"} 89.0
python_gc_collections_total{generation="1"} 8.0
python_gc_collections_total{generation="2"} 0.0
# HELP python_info Python platform information
# TYPE python_info gauge
python_info{implementation="CPython",major="3",minor="8",patchlevel="17",version="3.8.17"} 1.0
# HELP process_virtual_memory_bytes Virtual memory size in bytes.
# TYPE process_virtual_memory_bytes gauge
process_virtual_memory_bytes 2.62705152e+08
# HELP process_resident_memory_bytes Resident memory size in bytes.
# TYPE process_resident_memory_bytes gauge
process_resident_memory_bytes 2.7262976e+07
# HELP process_start_time_seconds Start time of the process since unix epoch in seconds.
# TYPE process_start_time_seconds gauge
process_start_time_seconds 1.68624463544e+09
# HELP process_cpu_seconds_total Total user and system CPU time spent in seconds.
# TYPE process_cpu_seconds_total counter
process_cpu_seconds_total 6.11
# HELP process_open_fds Number of open file descriptors.
# TYPE process_open_fds gauge
process_open_fds 6.0
# HELP process_max_fds Maximum number of open file descriptors.
# TYPE process_max_fds gauge
process_max_fds 1.048576e+06
# HELP flask_exporter_info Information about the Prometheus Flask exporter
# TYPE flask_exporter_info gauge
flask_exporter_info{version="0.22.4"} 1.0
# HELP flask_http_request_duration_seconds Flask HTTP request duration in seconds
# TYPE flask_http_request_duration_seconds histogram
flask_http_request_duration_seconds_bucket{le="0.005",method="GET",path="/hello",status="200"} 29.0
flask_http_request_duration_seconds_bucket{le="0.01",method="GET",path="/hello",status="200"} 29.0
flask_http_request_duration_seconds_bucket{le="0.025",method="GET",path="/hello",status="200"} 29.0
flask_http_request_duration_seconds_bucket{le="0.05",method="GET",path="/hello",status="200"} 29.0
flask_http_request_duration_seconds_bucket{le="0.075",method="GET",path="/hello",status="200"} 29.0
flask_http_request_duration_seconds_bucket{le="0.1",method="GET",path="/hello",status="200"} 29.0
flask_http_request_duration_seconds_bucket{le="0.25",method="GET",path="/hello",status="200"} 29.0
flask_http_request_duration_seconds_bucket{le="0.5",method="GET",path="/hello",status="200"} 29.0
flask_http_request_duration_seconds_bucket{le="0.75",method="GET",path="/hello",status="200"} 29.0
flask_http_request_duration_seconds_bucket{le="1.0",method="GET",path="/hello",status="200"} 29.0
flask_http_request_duration_seconds_bucket{le="2.5",method="GET",path="/hello",status="200"} 29.0
flask_http_request_duration_seconds_bucket{le="5.0",method="GET",path="/hello",status="200"} 29.0
flask_http_request_duration_seconds_bucket{le="7.5",method="GET",path="/hello",status="200"} 29.0
flask_http_request_duration_seconds_bucket{le="10.0",method="GET",path="/hello",status="200"} 29.0
flask_http_request_duration_seconds_bucket{le="+Inf",method="GET",path="/hello",status="200"} 29.0
flask_http_request_duration_seconds_count{method="GET",path="/hello",status="200"} 29.0
flask_http_request_duration_seconds_sum{method="GET",path="/hello",status="200"} 0.006836412016127724
flask_http_request_duration_seconds_bucket{le="0.005",method="GET",path="/jobs",status="200"} 4.0
flask_http_request_duration_seconds_bucket{le="0.01",method="GET",path="/jobs",status="200"} 9.0
flask_http_request_duration_seconds_bucket{le="0.025",method="GET",path="/jobs",status="200"} 11.0
flask_http_request_duration_seconds_bucket{le="0.05",method="GET",path="/jobs",status="200"} 11.0
flask_http_request_duration_seconds_bucket{le="0.075",method="GET",path="/jobs",status="200"} 11.0
flask_http_request_duration_seconds_bucket{le="0.1",method="GET",path="/jobs",status="200"} 11.0
flask_http_request_duration_seconds_bucket{le="0.25",method="GET",path="/jobs",status="200"} 11.0
flask_http_request_duration_seconds_bucket{le="0.5",method="GET",path="/jobs",status="200"} 11.0
flask_http_request_duration_seconds_bucket{le="0.75",method="GET",path="/jobs",status="200"} 11.0
flask_http_request_duration_seconds_bucket{le="1.0",method="GET",path="/jobs",status="200"} 11.0
flask_http_request_duration_seconds_bucket{le="2.5",method="GET",path="/jobs",status="200"} 11.0
flask_http_request_duration_seconds_bucket{le="5.0",method="GET",path="/jobs",status="200"} 11.0
flask_http_request_duration_seconds_bucket{le="7.5",method="GET",path="/jobs",status="200"} 11.0
flask_http_request_duration_seconds_bucket{le="10.0",method="GET",path="/jobs",status="200"} 11.0
flask_http_request_duration_seconds_bucket{le="+Inf",method="GET",path="/jobs",status="200"} 11.0
flask_http_request_duration_seconds_count{method="GET",path="/jobs",status="200"} 11.0
flask_http_request_duration_seconds_sum{method="GET",path="/jobs",status="200"} 0.07385792299828609
# HELP flask_http_request_duration_seconds_created Flask HTTP request duration in seconds
# TYPE flask_http_request_duration_seconds_created gauge
flask_http_request_duration_seconds_created{method="GET",path="/hello",status="200"} 1.6862446677038813e+09
flask_http_request_duration_seconds_created{method="GET",path="/jobs",status="200"} 1.6862446704012e+09
# HELP flask_http_request_total Total number of HTTP requests
# TYPE flask_http_request_total counter
flask_http_request_total{method="GET",status="200"} 40.0
# HELP flask_http_request_created Total number of HTTP requests
# TYPE flask_http_request_created gauge
flask_http_request_created{method="GET",status="200"} 1.6862446677039692e+09
# HELP flask_http_request_exceptions_total Total number of HTTP requests which resulted in an exception
# TYPE flask_http_request_exceptions_total counter
# HELP requests_by_status Request latencies by status
# TYPE requests_by_status summary
requests_by_status_count{status="200"} 29.0
requests_by_status_sum{status="200"} 0.00028225298956385814
# HELP requests_by_status_created Request latencies by status
# TYPE requests_by_status_created gauge
requests_by_status_created{status="200"} 1.6862446677038062e+09
* Closing connection 0

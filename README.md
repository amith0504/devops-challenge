# Assignment
## Your task is to accomplish the following:
- Build a small Kubernetes environment locally.  Please use whatever local k8s environment you would like (KiND, minikube, etc)
- Build Docker files for both sample applications (applications must return correct results)
- Use pulumi to deploy the pods to the cluster.  Please use whatever programming language you are most familiar with.
- Ensure the api microservice is exposed and reachable externally (ie: we should be able to access the api microservice from the laptop we are running it on).   Communication to the jobs microservice should be available from the api microservice
- Ensure the `JOBS_SERVICE` env var is present in the api container
- Make the process as automated as possible.  shell scripts, Makefiles, etc. are all acceptable.
- Please include instructions in the README.md for running the setup

# Bonus points
## If you have extra time and want to expand on some capabilities:
- Adding metrics and monitoring pod status (ie: prometheus)
- Harden containers / pods to best practices

# Notes:
- Please do not fork or submit a PR to this repo
- Be prepared to have a conversation about the challenge, as well as how you would automate this process even further with CI/CD
- Feel free to improve the python code
- If you get stuck or need more information, please reach out for clarity
- Have fun!

1. First  clone this project 
2. Build the docker images api and jobs devops-challenge/build-api/ and devops-challenge/build-jobs/ respectively .Since I am running in kind I have
   hardcoded the IP in the JOBS_SERVICE environmental variable. 
3. Push the docker images to dockerhub.
4. Run the pulumi up command to deploy the application in kuberenetes application. Pulumi context can be set to use kind (local docker environment)




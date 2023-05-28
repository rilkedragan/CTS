# Connectivity Test Service - CTS
Small Python application that recieves http GET request for URL that is passed as parameter __url__

CTS application is packed with Docekrfile and deployed to Google GKE cluster. Application is exposed as Kubernetes service.

Building Docker image:
 
 __docker build -t us.gcr.io/PROJECT-ID/ctsapp:TAG .__

 where __PROJECT-ID__ is Google Cloud project id and __TAG__ any desired value for tagging the image
 
 __Example of the response returned by CTS service running on Kubernetes cluster and port forwarded from the local port 8000:__

 curl http://localhost:8000/?url=https://portal.asgards-dev.tech -v
 
 ![image](https://github.com/rilkedragan/CTS/assets/126792923/86f5d18c-c783-4b45-af42-73fab0d6a7d6)

__Running application locally in Docker:__

![image](https://github.com/rilkedragan/CTS/assets/126792923/46c2fa4d-a6eb-477a-bf6f-c3e73dc24415)

Assumption is that any application using CTS for testing latency to desired URL would have logic to parse and interpret response from the CTS.

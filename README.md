# Connectivity Test Service - CTS
Small Python application that recives http GET request for URL that is passed as parameter

CTS application is packe with Docekrfile and deployed to Google GKE cluster. Application is exposed as Kubernetes service.

Building Docker image:
 
 __docker build -t us.gcr.io/PROJECT-ID/ctsapp:TAG .__

 where __PROJECT-ID__ is Google Cloud project id and __TAG__ any desired value for tagging the image
 
 Example of the response returned by CTS service running on Kubernetes cluster:

 curl http://localhost:8000/?url=https://portal.asgards-dev.tech -v
 ![image](https://github.com/rilkedragan/CTS/assets/126792923/86f5d18c-c783-4b45-af42-73fab0d6a7d6)

Assumption is that any application using CTS for testing latency to desired URL would have logic to parse and interpret response from the CTS.

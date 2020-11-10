#Dockerfile for the server
FROM python:3.7.9-slim

WORKDIR /client
COPY ./client/. .
RUN apt-get update
RUN apt-get install net-tools
RUN ifconfig eth0 192.168.2.2 netmask 255.255.255.0
CMD ["python3", "client.py"]

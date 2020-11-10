#Dockerfile for the server
FROM python:3.7.9-slim

WORKDIR /server
COPY ./serveur/. .
RUN apt-get update
RUN apt-get install net-tools
RUN ifconfig eth0 192.168.2.1 netmask 255.255.255.0
CMD ["python3", "server.py"]

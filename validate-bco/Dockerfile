# Container image that runs your code
#FROM alpine:3.10
FROM python:3

RUN pip install jsonschema jsonref

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY entrypoint.sh /entrypoint.sh
COPY validate_bco.py /validate_bco.py

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/entrypoint.sh"]

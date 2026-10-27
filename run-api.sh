#!/bin/sh
# Starts incident-api on its own. Used in Tasks 1 and 2.
docker rm -f incident-api >/dev/null 2>&1
docker run -d --name incident-api -p 8080:3000 incident-api:lab

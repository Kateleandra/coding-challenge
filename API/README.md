# API - User Manager Service

## How it works

This container has it's **VOLUME** mapped to /tmp. In this case, the API will store the _data.txt_ file into /tmp directory of the host machine, so the Cron Job can consume this file and add/remove the system users.

---

## Running this project

First, Build Docker Image:

```terminal
docker build --rm -f "Dockerfile" -t flask-app:latest .
```

Then, Run Docker Container inside the host machine.

with "--restart always" if the project must be kept running and automatic restart

```terminal
docker run -d --restart always -it -v /tmp:/tmp -p 8080:8080/tcp flask-app:latest
```

or using "--rm" if is needed to run once and the container doesn't need to be save after stopped

```terminal
docker run -d --rm -it -v /tmp:/tmp -p 8080:8080/tcp flask-app:latest
```

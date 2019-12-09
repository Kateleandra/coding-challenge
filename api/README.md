# API - User Manager Service

## About the API

This API was written using a lightweight WSGI framework: [FLASK](https://www.palletsprojects.com/p/flask/)!

## Code Analysis

All the project has been *formatted* using [_black_](https://black.readthedocs.io/en/stable/) and **statically validated** using [**pylint**](https://www.pylint.org/).

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
docker run -d --rm -it -v /tmp:/tmp -p 8080:8080 flask-app:latest
```

---

## Using the API

The API has a main route responding two verbs [**POST** and **DELETE**]

The API can be requested via many different interfaces, I.E.: _Postman Client_

* To submit a **new user** login entry to be added:

    Create a Postman [**POST**] request for:

    ```postman
    http://0.0.0.0:8080/user
    ```

    passing the following parameters in body as raw json:

    ```json
    {
        "name":"User Name",
        "login": "user.name",
        "password": "UGFzc3cwcmQwMTIzIQ=="
    }
    ```

    Be sure to send all parameters and a valid **Base64** password.

* To submit a **disable login** entry to be added:

    Create a Postman [**DELETE**] request for:

    ```postman
    http://0.0.0.0:8080/user
    ```

    passing the following parameters in body as raw json:

    ```json
    {
        "login": "user.name"
    }
    ```

    Be sure to send all parameters and a valid **Base64** password.
    Pay attention to the API Ip, it's 0.0.0.0 as a default route that points to the default route, which is, in this case the host machine IP. 
    
    Make sure to allow the port 8080 thought host's firewall. I.E: **sudo ufw allow 8080** if the host machine is _ubuntu_.

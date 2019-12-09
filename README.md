# CI&T - Coding Challenge

## Programme

> CI&T Application Project for Software Engineer Opening

---

## Aims of project

- This is a Linux-based project.
- Technologies used:
  - Python
  - Flask
  - Docker

## Nature of end-product

> Software: **Cron Job** and **Python WebAPI**

---

## Challenge

API - Will have both creation and removal routes for a login.
API Must be running inside a docker container exposed at port: 8080.

### add user route

- Name
- Login
- Temporary password (Base64)

### remote user route

- Login

Both routes will store into a file as shown bellow, that will be processed by a Cron Job everyday at midnight.

```yaml
ADD “Carla Alves Souza”, “carla.souza”, “Suporte123”
ADD “Mateus Santos Lima”, “mateus.lima1”, “Abcd234J01”
DISABLE “martim.ferreira”
```

Automation of new co-workers access to internal systems by adding or removing access via Cron Job once a day from a base file.

---

## Documentation

For API documentation head to [API](/api/README.md)

---

## TODO's

Incoming steps are:

* Implement TDD
* Write Postman Collection and Automated tests
* Write CRON Job for add/disable user login
# weather-api

A REST API to save and retrieve weather measurements (temperature and humidity)
from several sensors.

# Requirements

- Python 3.10
- Postgres 14.2

OR

- Docker
- Docker Compose

# Quick Start

## Clone the repository

```
$ git clone git@github.com:KNaiskes/weather-api.git
```

## Setup with Docker

```
$ cd weather-api/
$ docker-compose up -d
```

### Make migrations

```
$ docker-compose web python manage.py migrate
```

### Create super user

```
$ docker-compose web python createsuperuser
```

# HTTP Requests

**Base url:** localhost:8000/api/

**Authentication**

All requests must be authenticated with a token. After adding a new user from the
Django admin panel or CLI, a new token for this user is automatically created.
The token can be found through the admin panel or from the dbshell.

### Example

```
$ curl -X GET http://localhost:8000/api/sensors/ -H 'Authorization: Token 8608ab67a31be0feddb0031fbd32a207219005be'
```

## API paths table

| Path             | Method(s)        | Description                                                 |
|------------------|------------------|-------------------------------------------------------------|
| sensors/         | GET, POST        | Get all available sensor or add a new sensor                |
| sensors/*uuid*   | GET, PUT, DELETE | Get, update or delete a sensor based on its uuid            |
| metrics/*sensor* | GET              | Get all metrics from a particular sensor basend on its name |

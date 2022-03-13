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

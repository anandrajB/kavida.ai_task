<p align="center">
<img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FAST API"/>
<h2 align="center"> FastAPI Template </h2>

---
## About
This is a beginner's template for getting started with FastAPI.
It uses SQLAlchemy as the ORM. 

Contributions are welcome. 

## Features

- [x] Database Connection Using SQLAlchemy
- [x] FastAPI Server
- [x] Unit Testing with PyTest
- [x] Basic CRUD for Posts

<br>

## Dependencies

- Python 3.7+
- Pip
- Other listed in requirements.txt

## Running

- Clone the repo using

```bash
git clone https://github.com/mdhishaamakhtar/fastapi-sqlalchemy-postgres-template
```

- Create a Virtual Environment using

```bash
sudo pip install virtualenv
virtualenv env
```

- Activate the virtualenv

```bash
env\Scripts\activate # for windows
source env/bin/activate # for linux and mac
```

- Install dependencies

```bash
pip install -r requirements.txt
```

- Setting up environment variables

| Key     | Value |
| ----------- | ----------- |
| DATABASE_URL   | postgresql://user:password@host:port/db|

- To run the project

```bash
uvicorn main:app
```


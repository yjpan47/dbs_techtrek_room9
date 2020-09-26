### Overview

This repository serves at the backend API layer for [https://github.com/derekangziying/DBS-TEAM9](https://github.com/derekangziying/DBS-TEAM9)

All commits to this repository is down by the owner of this repository [yjpan47](https://github.com/yjpan47)

> There are two git usernames (**johnp** and **yjpan47**) that contributed to this repository - both belonging to the owner of this repository.

> Update: I have added the relevant secondary email to my github account. So all my commits should reflect **yjpan47** as the contributor now. 

This project is part of DBS TechTrek 2020.


### Setup Virtual Environment and Manage Dependencies

Make sure virtualenv is installed
```bash
pip install virtualenv
```

Create virtual environment named **venv**.
```bash
python3 -m venv venv
```

A **venv** should be created with the following structure:
```bash
venv
├── bin
├── include
├── lib
│   └── python3.6
│       └── site-packages
│           ├── easy_install.py
│           ├── pip
```

Activate virtual environment
```bash
source venv/bin/activate
```

Install all dependencies in **requirements.txt**
```bash
pip3 install wheel
pip3 install -r requirements.txt
```

### Create the Database

The location of the database is decided by the **DB_ENGINE_URL** variable in **config.py**.
By default, in **dev** environment, it will be a SQLite database located at **sqlite:///<current_directory>/api/main/local.db**.

We will be using alembic to autogenerate the database from python class models. 
FYI the class models can be found in **api/main/models/**.
```bash
pip3 install alembic
```
```bash
alembic revision --autogenerate -m "setup"
```
Go to **alembic/versions/** and observe that a new revision python script is generated. 
The python script has a function **upgrade** that will be called to spin up the database.
```bash
alembic upgrade head
```
**head** refers to the latest revision in **alembic/versions/**. You can also use the revision id e.g. *f0b6e910b613*.


### Run the Flask API Application

The application can be run from the root **main.py**. 
```bash
python3 main.py
```

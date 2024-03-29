# URL Shortener

![](https://img.shields.io/badge/lang-python-blue)
![](https://img.shields.io/badge/version-v0.2-blue)

Creating a URL shortener with Python and SQLite3. To setup the project you need to install
project requirements. After that you can setup project by executing ```python3 main.py```.
You will have your ```HTTP``` server on ```localhost:3000```. Just try to open it on your browser.

## Requirements

Install project requirements.

```shell
pip3 install -r requirements.txt
```

## Database

By creating a ```database``` module, we created our database reading methods in ```Query``` class,
which reads the sql queries from ```database/sql``` files.

## Frontend

Using javascript ```fetch``` to make ```http``` calls to our backend system.

## Backend

We created a simple ```rest-api``` with ```Flask``` framework in python and using ```MVC```
architecture.

## Docker

Use the following command to setup the project with ```Docker```.

```shell
docker compose up -d
```

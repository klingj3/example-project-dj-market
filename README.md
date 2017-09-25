# sdd-farmers
Forming community connections to support the local food movement.

## Getting Started
1. Create and activate a virtual environment called `devenv` where we'll install everything this project needs.
```bash
python3 -m venv devenv
source devenv/bin/activate
```

2. Install the development requirements.
```bash
pip install -r requirements.txt
```

## Useful Commands
* Run the server!
```bash
python manage.py runserver
```
* Initialize your database, or apply migrations.
```bash
python manage.py migrate
```
* Delete everything in your database.
```bash
python manage.py flush
```
* Create a new app.
First create the necessary folder inside `apps`.
```bash
mkdir market/apps/<app_name>
```
Then create the app.
```bash
python manage.py startapp <app_name> ./market/apps/<app_name>
```

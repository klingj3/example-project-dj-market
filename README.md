# Harvest Here
#### Forming community connections to support the local food movement.

## Getting Started
Requirements:
* Python 3.5

1. Create a virtual environment for this project with the command `virtualenv sdd-venv`.
2. User this virtual environment via the command: `source sdd-venv/bin/activate`. If successful, your terminal will now say (sdd-venv) at the beginning of each line.
3. Install all of the required packages and extensions, `sudo pip3 install -r requirements.txt`, from within your Harvest Here directory containing the requirements.txt file (where you will be if you've followed the instructions up to this point). This will take several minutes.
4. Change to the "market" directory, `cd market`.
5. Run the following two commands to get the database ready to go.
`python3 manage.py makemigrations`
`python3 manage.py migrate`
6. Everything should be ready! All that's left is to run the server via the command `python3 manage.py runserver` and the site will be available at http://localhost:8000.

## Useful Commands
* Run the server!
```bash
$ python3 manage.py runserver
```
* Initialize your database, or apply migrations.
```bash
$ python3 manage.py migrate
```
* Delete everything in your database.
```bash
$ python3 manage.py flush
```
* Create a new app.
First create the necessary folder inside `apps`.
```bash
$ mkdir market/apps/<app_name>
```
Then create the app.
```bash
$ python3 manage.py startapp <app_name> ./market/apps/<app_name>
```

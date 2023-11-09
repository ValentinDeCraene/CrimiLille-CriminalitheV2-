# Flask web app:
- A ready to use Flask SQL-Alchemy web app using a Sqlite 3 database.
- The purpose of this repository is simply to have the basic architecture of a Flask web app for future projects.
- Frontend: Bootstrap (5.0.2), JQuery

# Install:
- Install and create a virtual environment: `sudo apt-get install python3 libfreetype6-dev python3-pip python3-virtualenv && virtualenv ~/.flask_app`
- Activate your new virtualenv: `source ~/.flask_app/bin/activate`
- Install requirements: `pip install -r requirements.txt`
- Go to the app directory: `cd app `
- Launch on local host: `python3 run.py`
- Go to your local host: http://127.0.0.1:5000/

# Web app structure:
```
.
├── app
│   ├── app
│   │   ├── app.py
│   │   ├── constantes.py
│   │   ├── __init__.py
│   │   ├── modeles
│   │   │   ├── data.py
│   │   │   └── __init__.py
│   │   |
│   │   ├── routes
│   │   │   ├── api.py
│   │   │   ├── generic.py
│   │   │   ├── __init__.py
│   │   │   
│   │   ├── static
│   │   │   ├── css
│   │   │   ├── fonts
│   │   │   ├── images
│   │   │   └── js
│   │   └── templates
│   │       ├── container.html
│   │       ├── pages
│   │       │   └── index.html
│   │       └── partials
│   ├── bdd.db
│   ├── path.py
│   └── run.py
├── ReadMe.md
└── requirements.txt
```
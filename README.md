# Presentation Attendance.

### Topics

- Project Description
- Tech Stack
- Api Docs & Endpoints
- Setup & Installations

RESTful API for data for presentations and attendees at conferences.

## Description.

What you will be able to do:

- Create a presenation
- Create an attendee
- Add an attendee to the list of specific presentation.

## Tech Stack

- Python:
- Django
- PostgresSQL

## API Documentation & important endpoints.

- Link to Api documentation can be found [here](https://sucasa-presentation.herokuapp.com/api-docs/)
- Base url [https://sucasa-presentation.herokuapp.com/api/v1]

Important Endpoints

- `GET on base_url/presentation` provides a list of presentations with speakers and attendees
- `POST on base_url/presentation` creates a presentation
- `POST on base_url/attendee` creates an attendee to the presentation
- `PUT on base_url/presentations/:presentation_id/attendees/:attendee_id` Adds an attendee to a presentation

# Setup & Installations

### Setup your environment

```bash
virtualenv -p python3 env
```

### Activate your environment

```bash
source env/bin/activate
```

#### cd into project and install requirements.txt

```bash
pip install -r requirements.txt
```

#### create .env file and fill it with info in the .sample_env, then change the values.

```bash
.env
```

## Perform database migration:

```bash
python manage.py makemigration
python manage.py migrate
```

### Run Development Server

```bash
python manage.py runserver
```

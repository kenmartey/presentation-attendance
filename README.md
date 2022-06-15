# Presentation Attendance

## Setup

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

## Perform database migration:

```bash

python manage.py makemigration
python manage.py migrate
```

### Run Development Server

```bash
python manage.py runserver
```

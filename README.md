# django-todo
A simple todo app built with django

![todo App](https://raw.githubusercontent.com/shreys7/django-todo/develop/staticfiles/todoApp.png)

### Local Development Setup

To get this repository, run the following command inside your git enabled terminal:
```bash
git clone https://github.com/shreys7/django-todo.git
cd django-todo
```

#### Prerequisites
- Python 3.x
- pip

#### 1. Create a Virtual Environment
It is recommended to use a virtual environment to manage project dependencies.
```bash
python -m venv .venv
source .venv/bin/activate
```

#### 2. Install Dependencies
Install the required packages using pip:
```bash
pip install -r requirements.txt
```

#### 3. Configure Environment Variables
Create a `.env` file in the root of the project:
```bash
touch .env
```

Open the `.env` file and add the following variables.

```
# .env

# Generate a new secret key for your project.
# You can use the following command in your terminal to generate one:
# python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
SECRET_KEY=your-secret-key-here

# Set to True for development to get detailed error messages
DEBUG=True
```

**Important:** The `SECRET_KEY` is a critical security component for any Django application. The key provided above is an example and should be replaced with a unique, randomly generated key.

#### 4. Database Migrations
Apply the database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

#### 5. Create a Superuser
Create an admin user to access the Django admin interface:
```bash
python manage.py createsuperuser
```
You will be prompted to enter a username, email, and password for the admin user.

#### 6. Run the Development Server
Start the Django development server:
```bash
python manage.py runserver
```

Once the server is running, you can access the app at [http://127.0.0.1:8000/todos](http://127.0.0.1:8000/todos).

Cheers and Happy Coding :)

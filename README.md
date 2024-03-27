# novel_api project

Create a novel api in Django Framework

# Create the project directory

`mkdir novel_api`<br>
`cd novel_api`

# Create a virtual environment to isolate our package dependencies locally

`python3 -m venv env`<br>
`source env/bin/activate` # On Windows use `env\Scripts\activate`

# Install Django and Django REST framework into the virtual environment

`pip install django`<br>
`pip install djangorestframework
`

# Set up a new project with a single application (Note the trailing '.' character)

`django-admin startproject novel_api .`<br>
`cd novel_api`<br>
`django-admin startapp backend`<br>
`cd ..`
# API-project-demo
Employee Management REST API

A RESTful API built using Django Rest Framework to manage employees in a company.
The API supports CRUD operations, JWT-based authentication, filtering, pagination, and unit testing.

Features

Create, Read, Update, Delete (CRUD) employees

JWT-based Authentication

Pagination (10 employees per page)

Filtering by department and role

Proper error handling with HTTP status codes

Unit tests for all endpoints

Tested using Postman and Python requests

Tech Stack

Language: Python 3.x

Framework: Django, Django REST Framework

Authentication: JWT (SimpleJWT)

Database: SQLite

Testing: DRF APITestCase

API Client: Postman

Project Structure

employee_api/

employee_api/

settings.py

urls.py

employees/

models.py

serializers.py

views.py

urls.py

tests.py

manage.py

requirements.txt

README.md

Installation and Setup

Clone the repository

git clone https://github.com/missionproject1/API-project-demo.git

cd employee_api

Create virtual environment

python -m venv venv
venv\Scripts\activate (Windows)

Install dependencies

pip install -r requirements.txt

Run migrations

python manage.py makemigrations
python manage.py migrate

Create superuser

python manage.py createsuperuser

Start server

python manage.py runserver

Server runs at:
http://127.0.0.1:8000/

Authentication (JWT)

Get access token

POST /api/token/

Request body:
{
"username": "your_username",
"password": "your_password"
}

Use the access token in request headers:

Authorization: Bearer <access_token>

API Endpoints

POST /api/employees/ Create employee
GET /api/employees/ List all employees
GET /api/employees/{id}/ Retrieve single employee
PUT /api/employees/{id}/ Update employee
DELETE /api/employees/{id}/ Delete employee

Filtering and Pagination

Filter by department:
/api/employees/?department=HR

Filter by role:
/api/employees/?role=Developer

Pagination:
/api/employees/?page=2

Running Tests

python manage.py test

Tests include:

CRUD operations

Authentication

Duplicate email validation

404 handling for invalid IDs

Manual Testing

Tested using Postman

Tested using Python requests script

Live demo shown using Postman

Presentation Flow (Interview Demo)

Generate JWT token

Create employee (201 Created)

Handle duplicate email (400 Bad Request)

List employees with pagination and filtering

Retrieve employee by ID (200 / 404)

Update employee details

Delete employee (204 No Content)

Design Decisions

Followed RESTful principles

Used ModelSerializer for validation

Explicit HTTP status codes

Secure endpoints using JWT authentication

Clean and modular code structure

Author

Prathamesh Patkar
Python Backend Developer

License

This project is created for technical evaluation and learning purposes.
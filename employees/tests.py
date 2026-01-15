from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Employee

class EmployeeAPITest(APITestCase):

    def setUp(self):
        # Create user
        self.user = User.objects.create_user(
            username='test',
            password='test123'
        )

        # JWT token
        refresh = RefreshToken.for_user(self.user)
        access_token = str(refresh.access_token)

        # Attach token
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + access_token
        )

        # Sample employee
        self.employee = Employee.objects.create(
            name="John",
            email="john@test.com",
            department="HR",
            role="Manager"
        )

    # ---------- CREATE ----------
    def test_create_employee(self):
        data = {
            "name": "Alice",
            "email": "alice@test.com",
            "department": "Engineering",
            "role": "Developer"
        }
        response = self.client.post('/api/employees/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_duplicate_email(self):
        data = {
            "name": "Duplicate",
            "email": "john@test.com"
        }
        response = self.client.post('/api/employees/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # ---------- GET LIST ----------
    def test_get_all_employees(self):
        response = self.client.get('/api/employees/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data['results']), 1)

    # ---------- GET SINGLE ----------
    def test_get_single_employee(self):
        response = self.client.get(f'/api/employees/{self.employee.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "John")

    def test_get_employee_not_found(self):
        response = self.client.get('/api/employees/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # ---------- UPDATE ----------
    def test_update_employee(self):
        data = {
            "name": "John Updated",
            "email": "john@test.com",
            "department": "Sales",
            "role": "Lead"
        }
        response = self.client.put(
            f'/api/employees/{self.employee.id}/',
            data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['department'], "Sales")

    # ---------- DELETE ----------
    def test_delete_employee(self):
        response = self.client.delete(
            f'/api/employees/{self.employee.id}/'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

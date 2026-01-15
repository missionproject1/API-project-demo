from django.urls import path
from .views import employee_list, employee_details

urlpatterns = [
    # List all employees / Create employee
    path('employees/', employee_list, name='employee-list'),

    # Get / Update / Delete single employee
    path('employees/<int:pk>/', employee_details, name='employee-details'),
]
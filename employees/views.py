from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from .models import Employee
from .serializers import EmployeeSerializer


@api_view(['GET', 'POST'])
def employee_list(request):

    if request.method == 'GET':
        queryset = Employee.objects.all()

        department = request.query_params.get('department')
        role = request.query_params.get('role')

        if department:
            queryset = queryset.filter(department=department)
        if role:
            queryset = queryset.filter(role=role)

        paginator = PageNumberPagination()
        paginator.page_size = 10
        paginated_qs = paginator.paginate_queryset(queryset, request)

        serializer = EmployeeSerializer(paginated_qs, many=True)
        return paginator.get_paginated_response(serializer.data)

    elif request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


   
@api_view(['GET', 'PUT', 'DELETE'])
def employee_details(request, pk):

    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response(
            {"error": "Employee not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    #  GET REQUEST
    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)

    #  PUT REQUEST
    elif request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #  DELETE REQUEST
    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
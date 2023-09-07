from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.viewsets import ModelViewSet


class EmployeeCRUDCBV(ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

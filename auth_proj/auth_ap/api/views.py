from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeCRUDCBV(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

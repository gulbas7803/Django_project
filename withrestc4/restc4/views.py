from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, DjangoModelPermissions
from restc4.permissions import IsReadOnly, IsGetOrPatch, GulbasPermission


#from rest_framework_jwt.authentication import JSONWebTokenAuthentication


# from rest_framework.authentication import SessionAuthentication


# Create your views here.

class EmployeeCRUDCBV(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [TokenAuthentication, ]
    # permission_classes = [IsAdminUser, ]
    permission_classes = [GulbasPermission, ]

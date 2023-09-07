from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from .custompermissions import MyPermission
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions


# Create your views here.

# class StudentModelViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly]
#     # permission_classes = [IsAuthenticatedOrReadOnly]

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated, ]
    # permission_classes = [IsAdminUser]
    # permission_classes = [DjangoModelPermissions]
    permission_classes = [MyPermission]


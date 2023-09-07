# from django.shortcuts import render
from school_management_app.models import RegisterStudent
from school_management_app.api.serializers import Register_Serializer, Login_Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class StudentListView(APIView):
    def get(self, request):
        Student_list = RegisterStudent.objects.all()
        serializer = Register_Serializer(Student_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = Register_Serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetailView(APIView):
    def get(self, request, pk):
        try:
            student = RegisterStudent.objects.get(id=pk)
        except RegisterStudent.DoesNotExist:
            stud_data = {"message": "Request resource not avalibal"}
            return Response(stud_data, status=status.HTTP_404_NOT_FOUND)

        serializer = Register_Serializer(student)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_by_object(self, pk):
        try:
            student = RegisterStudent.objects.get(id=pk)
        except RegisterStudent.DoesNotExist:
            student = None
        return student

    def put(self, request, pk):
        student = self.get_by_object(pk)
        if student is None:
            dict_data = {"message": "Request resource not avalibal to Update"}
            return Response(dict_data, status=status.HTTP_404_NOT_FOUND)
        serializer = Register_Serializer(RegisterStudent, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_by_object(id=pk)
        if student is None:
            stud_data = {"message": "Request resource not avalibal to delete"}
            return Response(stud_data, status=status.HTTP_404_NOT_FOUND)
        student.delete()
        stud_data = {"message": "Request resource deleted successfully"}
        return Response(stud_data, status=status.HTTP_204_NO_CONTENT)

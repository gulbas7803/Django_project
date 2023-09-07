from django.shortcuts import render
import io
from django.views.generic import View
from rest_framework.parsers import JSONParser
from restapi1.rest1.models import Employees
from restapi1.rest1.serializers import EmployeesSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.
class EmployeesCRUDCBV(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        id = pdata.get('id', None)
        if id is not None:
            emp = Employees.objects.get(id=id)
            serializer = EmployeesSerializer(emp)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        qs = Employees.objects.all()
        serializer = EmployeesSerializer(qs,many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

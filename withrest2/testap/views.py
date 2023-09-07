from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# from testap.serializers import NameSerializer
from .serializers import NameSerializers


# Create your views here.
class TestApiView(APIView):
    def get(self, request, *args, **kwargs):
        colors = ['red', 'green', 'blue', 'yellow']
        return Response({'msg': 'Happy Pongal', 'colors': colors})

    def post(self, request, *args, **kwargs):
        serializer = NameSerializers(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            msg = 'Hello {}, Happy Pongal'.format(name)
            return Response({'msg': msg}, status=201)
        else:
            return Response(serializer.errors, status=400)

    def put(self, request, *args, **kwargs):
        return Response({'msg': 'this msg from put method of api view'})

    def patch(self, request, *args, **kwargs):
        return Response({'msg': 'this msg from patch method of api view'})

    def delete(self, request, *args, **kwargs):
        return Response({'msg': 'this msg from delete method of api view'})


from rest_framework.viewsets import ViewSet


class TetsViewSet(ViewSet):
    def list(self, request):
        colors = ['red', 'green', 'blue', 'yellow']
        return Response({'msg': 'Happy New Year', 'colors': colors})

    def create(self, request):
        serializer = NameSerializers(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            msg = 'Hello {}, Happy New Year 2023!!!'.format(name)
            return Response({'msg': msg}, status=201)
        else:
            return Response(serializer.errors, status=400)

    def retrieve(self,request,pk=None):
        return Response({'msg': 'this response from retrieve method of  viewset'})
    def update(self,request,pk=None):
        return Response({'msg': 'this response from update method of  viewset'})
    def partial_update(self,request,pk=None):
        return Response({'msg': 'this response from partial_update method of  viewset'})
    def destroy(self,request,pk=None):
        return Response({'msg': 'this response from destroy method of  viewset'})

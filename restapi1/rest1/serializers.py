from rest_framework import serializers

class EmployeesSerializer(serializers.Serializer):
    eno = serializers.IntegerField()
    ename = serializers.CharField(max_length=100)
    esal = serializers.FloatField()
    eaddr = serializers.CharField(max_length=100)

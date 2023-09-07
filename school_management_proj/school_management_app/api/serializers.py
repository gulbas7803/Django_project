from rest_framework import serializers
from school_management_app.models import Register, Login


class Register_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'


class Login_Serializer(serializers.ModelSerializer):
    class Meta:
        models = Login
        fields = '__all__'

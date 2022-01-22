from rest_framework.serializers import ModelSerializer

from .models import User

class UserSerial(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email','password']
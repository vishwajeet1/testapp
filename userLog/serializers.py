from rest_framework import serializers
from userLog.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['created', 'firstName', 'lastName', 'mobile', 'email','password']

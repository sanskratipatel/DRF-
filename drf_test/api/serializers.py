from rest_framework import serializers 
from users.models import  user


class UsersSerializers (serializers.ModelSerializer):
    class Meta: 
        model = user
        fields = "__all__" 
    
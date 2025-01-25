from rest_framework import serializers
from .models import todo 
from django.contrib.auth import get_user_model

User = get_user_model()

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = todo
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    #todos is realeated name in ForenKey
    todos = TodoSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = '__all__'
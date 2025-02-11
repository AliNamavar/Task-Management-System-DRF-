from rest_framework import serializers
from .models import todo 
from django.contrib.auth import get_user_model

User = get_user_model()

class TodoSerializer(serializers.ModelSerializer):

    def validate_priority(self, priority):
        if priority < 10 or priority > 20:
            raise serializers.ValidationError("priority cant most be in range 10 to 20")
        return priority

    class Meta:
        model = todo
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    todos = TodoSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = '__all__'
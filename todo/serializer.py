from rest_framework import serializers
from .models import todo 


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = todo
        fields = ['title', 'content']

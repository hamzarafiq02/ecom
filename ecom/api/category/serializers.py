from rest_framework import serializers
from .models import category

class categorySerializer(serializers.Serializer):
    class Meta:
        model = category
        field = ('name', 'description')
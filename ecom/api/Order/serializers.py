from rest_framework import serializers
from .models import Order

class productSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model:Order
        field=('user')
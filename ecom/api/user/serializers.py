from ast import Not
from dataclasses import field
from multiprocessing.sharedctypes import Value
from pyexpat import model
from tokenize import Comment
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import authentication_classes, permission_classes
from .models import customuser

class userSerializer(serializers.HyperlinkedModelSerializer):
    
     def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set.password(password)
            instance.save()
            return instance

     def update(self, instance, validated_data):
        for attr, Value in validated_data.items():
            if attr == 'password':
                instance.set_password(Value)
            else:
                setattr(instance, attr, Value)
        instance.save()
        return instance
    
    
     class Meta:
        model = customuser
        extra_kwarge = {'password': {'write_only':True}}
        field  = ('name', 'email', 'password', 'phone', 'gender', 'is_active', 'is_staff', 'is_superuser')
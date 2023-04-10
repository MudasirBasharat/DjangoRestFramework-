from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import studentmodel

class studentserialzer(serializers.ModelSerializer):
    class Meta:
        model=studentmodel
        fields=['id','name','rollnbr','city']
            
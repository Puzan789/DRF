from rest_framework import serializers
from .models import *
class studentserializer(serializers.ModelSerializer):
    class Meta:
        model=student
        fields='__all__'
        # exclude
    def validate(self,data):
        if data['age'] < 18 :
            raise serializers.ValidationError({'error':'age cannot be less than 18'})
        
        if any(char.isdigit() for char in data['name']):
            raise serializers.ValidationError({'error':'name cannot contains digit '})
        return data
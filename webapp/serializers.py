from rest_framework import serializers
from .models import employees  # Correctly import the model from your app's models.py

class employeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = employees
        fields = ('__all__')  # Corrected spelling and included fields

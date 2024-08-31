from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response  # Correct import for the Response class
from rest_framework import status  # Correct import for status codes
from .models import employees  # Import the employees model from your app's models.py
from .serializers import employeesSerializer  # Import the employeesSerializer from your app's serializers.py

class employeesList(APIView):  # Using plural form for the class name
    def get(self, request):
        employees_list = employees.objects.all()  # Use the model class correctly
        serializer = employeesSerializer(employees_list, many=True)  # Serialize the list of employees
        return Response(serializer.data)  # Return serialized data as JSON
    
    def post(self, request):  # Added 'request' as a parameter to the post method
        serializer = employeesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

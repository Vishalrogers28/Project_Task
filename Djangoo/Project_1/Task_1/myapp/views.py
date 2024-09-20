from django.shortcuts import render
from myapp.models import MyModel

print("Creating MyModel instance...")
instance = MyModel.objects.create(name="Test Instance")
print("Instance created successfully.")


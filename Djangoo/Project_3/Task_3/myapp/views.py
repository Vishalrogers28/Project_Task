from django.shortcuts import render
from myapp.models import MyModel

try:
    print("Creating MyModel instance...")
    instance = MyModel.objects.create(name="Test Transaction")
except Exception as e:
    print(f"Exception caught: {e}")

if MyModel.objects.filter(name="Test Transaction").exists():
    print("Instance was saved.")
else:
    print("Instance was not saved due to transaction rollback.")



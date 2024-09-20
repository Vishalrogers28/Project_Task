from django.shortcuts import render
from myapp.models import MyModel
import threading

print(f"Caller Thread ID: {threading.get_ident()}")
MyModel.objects.create(name="Test Instance")


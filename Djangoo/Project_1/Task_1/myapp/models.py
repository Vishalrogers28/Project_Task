from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import time

# Create your models here.
class MyModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


@receiver(post_save, sender=MyModel)
def my_signal_receiver(sender, instance, **kwargs):
    print("Signal received. Starting long-running task.")
    time.sleep(5)  
    print("Long-running task completed.")


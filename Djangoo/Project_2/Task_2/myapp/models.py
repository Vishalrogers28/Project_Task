from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import threading

class MyModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


@receiver(post_save, sender=MyModel)
def my_signal_receiver(sender, instance, **kwargs):

    print(f"Signal Receiver Thread ID: {threading.get_ident()}")
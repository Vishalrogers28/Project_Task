from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

class MyModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


@receiver(post_save, sender=MyModel)
def my_signal_receiver(sender, instance, **kwargs):
    print("Signal received. Raising an exception to test transaction rollback.")
    raise Exception("Triggering rollback in signal.")
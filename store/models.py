from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_store_id_generator
from accounts.models import Employee
# Create your models here.


class Store(models.Model):
    name = models.CharField(max_length=30, unique=True,verbose_name="Store name")
    capacity = models.IntegerField(default=0, verbose_name="Capacity")
    number_of_items = models.IntegerField(default=0)
    manager = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="Manager")
    store_id = models.CharField(max_length=10,
                                primary_key=True, null=False)
    store_users = models.ManyToManyField(Employee)

    def __str__(self):
        return self.name


def pre_save_create_store_id(sender, instance, *args, **kwargs):
    if not instance.store_id:
        instance.store_id = unique_store_id_generator(instance)


pre_save.connect(pre_save_create_store_id, sender=Store)

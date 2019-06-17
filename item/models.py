from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save
from .utils import unique_item_id_generator
from store.models import Store
from accounts.models import Employee
# Create your models here.


class Item(models.Model):

    WEIGHT_CLASSES = [
        ("kg", "Kilograms"),
        ("g", "Grams"),
        ("t", "Tonnes"),
    ]
    ITEM_CLASSES = [
        ("A", "Electronics"),
        ("B", "Chemicals"),
        ("C", "Books"),
        ("D", "Clothing"),
        ("E", "Food"),
        ("F", "Other"),
    ]
    item_store = models.ForeignKey(Store, on_delete=models.CASCADE)
    added_by = models.ForeignKey(Employee, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="Item name")
    item_num = models.IntegerField(verbose_name="No. of units")
    date_stored = models.DateTimeField(
        verbose_name="Date of entry", default=timezone.now)
    date_removed = models.DateTimeField(null=True)
    fragile = models.BooleanField(verbose_name="Fragile")
    weight = models.DecimalField(
        verbose_name="Weight", decimal_places=2, max_digits=5)
    units = models.CharField(
        max_length=20, verbose_name="Units", choices=WEIGHT_CLASSES, null=False, blank=False)
    item_class = models.CharField(
        max_length=1,
        verbose_name="Item class",
        choices=ITEM_CLASSES,
        default="A")
    item_id = models.CharField(max_length=10, verbose_name="Item ID",
                               primary_key=True, null=False)

    def __str__(self):
        return self.item_id


def pre_save_create_item_id(sender, instance, *args, **kwargs):
    if not instance.item_id:
        instance.item_id = unique_item_id_generator(instance)


pre_save.connect(pre_save_create_item_id, sender=Item)

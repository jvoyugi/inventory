from django.utils.crypto import get_random_string
import re
from django.db.models import Q


def random_string_generator():
    return get_random_string(length=10, allowed_chars="ABCDEF0123456789")


def unique_item_id_generator(instance):
    item_new_id = random_string_generator()

    Item = instance.__class__

    qs_exists = Item.objects.filter(item_id=item_new_id).exists()
    if qs_exists:
        return unique_item_id_generator(instance)
    return item_new_id

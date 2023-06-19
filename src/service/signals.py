from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver
from service.models import Book


"""Book`s images compressor"""


@receiver(post_save, sender=Book)
def image_compressor(sender, **kwargs):
    if kwargs["created"]:
        with Image.open(kwargs["instance"].image.path) as photo:
            photo.save(kwargs["instance"].image.path, optimize=True, quality=50)

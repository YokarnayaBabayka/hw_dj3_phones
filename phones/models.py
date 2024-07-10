from django.db import models
from django.utils.text import slugify

class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=None)
    image = models.URLField(default=None)
    release_date = models.DateField(default=None)
    lte_exists = models.BooleanField(default=None)
    slug = models.SlugField(max_length = 70, unique=True)


    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)

from django.db import models
from django.db.models.deletion import PROTECT

# Create your models here.


class Category(models.Model):
    category = models.CharField(blank=False, null=False, max_length=64)

    def regards_count(self):
        return self.regards_set.count()

    def __str__(self) -> str:
        return self.category


class Regards(models.Model):
    regard_image = models.ImageField(upload_to="Regards")
    category = models.ForeignKey(Category, on_delete=PROTECT)

    def __str__(self) -> str:
        return f"{self.id} {self.category}"

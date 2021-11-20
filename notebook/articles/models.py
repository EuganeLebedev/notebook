from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    slug = models.SlugField(max_length=255, unique=True, null=False,
                            db_index=True, verbose_name='Title')
    post_content = models.TextField(blank=False)
    categoryes = models.ManyToManyField('Category', related_name='Categoryes')

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(self, *args, **kwargs)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'pk': self.slug})


class Category(models.Model):
    category_name = models.CharField(blank=False, max_length=255)

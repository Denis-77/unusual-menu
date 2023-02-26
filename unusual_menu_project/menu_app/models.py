from django.core.validators import validate_unicode_slug, RegexValidator, validate_slug
from django.db import models


class Menu(models.Model):
    name = models.CharField('Title', max_length=100)
    url = models.CharField('URL', max_length=255, validators=(validate_slug,))
    full_url = models.CharField('FULL_URL', max_length=255, blank=True, null=True)
    parent = models.ForeignKey('Menu', on_delete=models.CASCADE, blank=True, null=True)
    parent_url = models.CharField("Parent's URL", max_length=255, blank=True, null=True)
    level = models.PositiveIntegerField('level', default=1)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('level', )

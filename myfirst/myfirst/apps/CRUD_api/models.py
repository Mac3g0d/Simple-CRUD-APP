
from django.db import models


# Create your models here.


class CRUD_api(models.Model):
    name = models.CharField('name', max_length=255, blank=True, null=True)
    surname = models.CharField('surname', max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    position = models.CharField('position', max_length=40)

    def __str__(self):
        return self.name
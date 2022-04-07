from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name

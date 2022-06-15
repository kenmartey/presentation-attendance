from django.db import models


class CommonProfileInfo(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    email = models.EmailField()

    class Meta:
        abstract = True

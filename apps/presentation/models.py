from django.db import models
from django.contrib.postgres.fields import ArrayField

from sucasapresentation.utilities.models.timeStamp import TimeStampedModel


class Presentation(TimeStampedModel):
    presentation = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
    room = models.IntegerField()
    speakers = ArrayField(
        models.JSONField(), blank=True, null=True
    )

    def __str__(self):
        return f'{self.presentation}'

    class Meta:
        verbose_name_plural = 'Presentations'

from django.db import models
from sucasapresentation.utilities.models.commonProfileInfo import CommonProfileInfo

from sucasapresentation.utilities.models.timeStamp import TimeStampedModel


class Attendee(CommonProfileInfo, TimeStampedModel):
    registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Attendees'

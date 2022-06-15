from django.db import models

from apps.attendee.models import Attendee
from apps.presentation.models import Presentation
from sucasapresentation.utilities.models.commonProfileInfo import CommonProfileInfo


from sucasapresentation.utilities.models.timeStamp import TimeStampedModel


class PresentationAttendance(TimeStampedModel, CommonProfileInfo):
    presentation = models.ForeignKey(
        Presentation, on_delete=models.CASCADE,
        related_name='attendees')

    def __str__(self):
        return f'{self.presentation.presentation}'

    class Meta:
        verbose_name_plural = 'Presentation Attendance'

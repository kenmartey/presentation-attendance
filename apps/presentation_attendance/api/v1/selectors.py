
from rest_framework.exceptions import APIException
from rest_framework import status

from apps.attendee.models import Attendee
from apps.presentation.models import Presentation


class NotFoundValidationError(APIException):
    status_code = status.HTTP_404_NOT_FOUND


def query_attendee(attendee_id):
    try:
        return Attendee.objects.get(pk=attendee_id)
    except Attendee.DoesNotExist:
        raise NotFoundValidationError("Attendee does not exist")


def query_presentation(presentation_id):
    try:
        return Presentation.objects.get(pk=presentation_id)
    except Presentation.DoesNotExist:
        raise NotFoundValidationError("Presentation does not exist")

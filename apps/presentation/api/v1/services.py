
from apps.attendee.models import Attendee
from apps.presentation.models import Presentation
from .selectors import query_attendee, query_presentation


def add_attendee_to_presentation(presentation_id, attendee_id):
    attendee = query_attendee(attendee_id)
    presentation = query_presentation(presentation_id)
    Attendee.objects.create()
    presentation.attendees = attendee
    presentation.save()
    return presentation

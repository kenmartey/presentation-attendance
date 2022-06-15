
from apps.attendee.models import Attendee
from apps.presentation.models import Presentation
from apps.presentation_attendance.models import PresentationAttendance
from .selectors import query_attendee, query_presentation


def add_attendee_to_presentation(presentation_id, attendee_id):
    attendee = query_attendee(attendee_id)
    presentation = query_presentation(presentation_id)
    response = PresentationAttendance.objects.create(
        presentation=presentation, name=attendee.name, company=attendee.company, email=attendee.email)
    return response

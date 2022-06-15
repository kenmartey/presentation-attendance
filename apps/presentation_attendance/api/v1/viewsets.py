from rest_framework import viewsets, status
from rest_framework.response import Response
from apps.presentation_attendance.api.v1.services import add_attendee_to_presentation

from apps.presentation_attendance.models import PresentationAttendance

from .serializers import PresentationAttendanceSerializer


class PresentationAttendanceViewSet(viewsets.ModelViewSet):
    queryset = PresentationAttendance.objects.all()
    serializer_class = PresentationAttendanceSerializer

    def create(self, request, presentation_id, attendee_id):
        response = add_attendee_to_presentation(presentation_id, attendee_id)
        serializer = PresentationAttendanceSerializer(response)

        return Response({
            'detail': 'Attendee added to presentation successfully.'},
            status=status.HTTP_201_CREATED)

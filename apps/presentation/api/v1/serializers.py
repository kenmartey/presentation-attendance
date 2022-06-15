from rest_framework import serializers
from apps.presentation.models import Presentation
from apps.presentation_attendance.api.v1.serializers import PresentationAttendanceSerializer


class PresentationSerializer(serializers.ModelSerializer):
    attendees = PresentationAttendanceSerializer(many=True, read_only=True)

    class Meta:
        model = Presentation
        fields = ("id", "presentation", "details",
                  "room", "created_date", "modified",
                  "speakers", "attendees")

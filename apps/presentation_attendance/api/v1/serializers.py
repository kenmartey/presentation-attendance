from rest_framework import serializers
from apps.presentation.models import Presentation
from apps.presentation_attendance.models import PresentationAttendance


class PresentationAttendanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = PresentationAttendance
        fields = ("id", "name", "company", "email")

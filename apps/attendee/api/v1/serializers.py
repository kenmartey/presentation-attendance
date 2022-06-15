from rest_framework import serializers
from apps.attendee.models import Attendee


class AttendeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attendee
        fields = ('__all__')

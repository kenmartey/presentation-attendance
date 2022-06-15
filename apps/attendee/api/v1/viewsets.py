from django.shortcuts import render
from rest_framework import viewsets, status

from .serializers import Attendee, AttendeeSerializer


class PresentationViewSet(viewsets.ModelViewSet):
    queryset = Attendee.objects.all()
    serializer_class = AttendeeSerializer

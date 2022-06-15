from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from .viewsets import PresentationAttendanceViewSet


router = DefaultRouter()
add_attendee_to_presentation = PresentationAttendanceViewSet.as_view({
    "post": "create"})

urlpatterns = [
    path(r"", include(router.urls)),
    path("presentation/<int:presentation_id>/attendees/<int:attendee_id>",
         add_attendee_to_presentation,
         name="attendee_to_presentation"),
]

from rest_framework import viewsets

from apps.presentation.models import Presentation
from .serializers import PresentationSerializer


class PresentationViewSet(viewsets.ModelViewSet):
    queryset = Presentation.objects.all()
    serializer_class = PresentationSerializer

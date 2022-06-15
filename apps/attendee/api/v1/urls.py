from rest_framework.routers import DefaultRouter
from .viewsets import PresentationViewSet

router = DefaultRouter()
router.register(r'attendees', PresentationViewSet, basename='attendees')
urlpatterns = router.urls

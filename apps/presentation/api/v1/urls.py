from rest_framework.routers import DefaultRouter
from .viewsets import PresentationViewSet

router = DefaultRouter()
router.register(r'presentation', PresentationViewSet,
                basename='presentation')

urlpatterns = router.urls

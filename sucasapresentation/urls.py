"""sucasapresentation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


API_BASE_URL = 'api'

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'{API_BASE_URL}/v1/', include("apps.presentation.api.v1.urls")),
    path(f'{API_BASE_URL}/v1/', include("apps.attendee.api.v1.urls")),
    path(f'{API_BASE_URL}/v1/',
         include("apps.presentation_attendance.api.v1.urls")),

]

# swagger api doc
api_info = openapi.Info(
    title="Sucasa Presentation API",
    default_version="v1",
    description="API documentation for Sucasa Presentation",
)

schema_view = get_schema_view(
    api_info,
    public=True,

)
urlpatterns += [
    path("api-docs/", schema_view.with_ui("swagger",
         cache_timeout=0), name="api_docs")
]

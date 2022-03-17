"""spotify URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from base.views import AlbumViewSet, AuthorViewSet, MusicViewSet

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register('album', AlbumViewSet)
router.register('author',AuthorViewSet)
router.register('music',MusicViewSet)


schema_view = get_schema_view(
   openapi.Info(
      title="Spotify API",
      default_version='v1',
      description="This is Spotify clone API. \n You may use this API on public!!!",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact("Ravshanbek Madaminov <ravshanbekmadaminov68@gmail.com> <+998903036415>"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('documentation/',schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('documentation/redoc/',schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-ui'),

]

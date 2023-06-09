"""
URL configuration for ristto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from menu import views

router = routers.DefaultRouter()
router.register(r'items', views.ItemViewSet, 'items')
# * Only viewsets can be registered to a router

urlpatterns = [
    path('admin/', admin.site.urls),

    # External apps
    path("__reload__/", include("django_browser_reload.urls")),

    # Local apps
    path('menu/', include('menu.urls')),

    # REST Framework
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
    path('api/menu', views.CategoryList.as_view(), name='menu'),
]

# Serve media files in development server
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# TODO: setup for production (https://testdriven.io/blog/django-static-files/)
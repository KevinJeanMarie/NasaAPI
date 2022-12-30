from django.urls import path, include
from rest_framework import routers
from nasa.views import NasaViewSet

router = routers.DefaultRouter()
router.register('nasas', NasaViewSet)

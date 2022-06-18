from django.urls import path, include
from rest_framework import routers

from .views import InmuebleViewSet


router = routers.DefaultRouter()
router.register('inmuebles', InmuebleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
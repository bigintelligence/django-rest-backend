from django.urls import path, include
from rest_framework import routers

from .views import InmuebleViewSet, UploadCSVViewSet


router = routers.DefaultRouter()
router.register('inmuebles', InmuebleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('carga/', UploadCSVViewSet.as_view())
]
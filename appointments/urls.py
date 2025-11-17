# App-level routing

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, ProviderViewSet, AppointmentViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'providers', ProviderViewSet)
router.register(r'appointments', AppointmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import include ,path
from rest_framework import routers
from .views import InformationViewSet, MotherViewSet, NotificationViewSet

router =routers.DefaultRouter()
router.register(r'mother',MotherViewSet)

router =routers.DefaultRouter()
router.register(r'information',InformationViewSet)

router =routers.DefaultRouter()
router.register(r'notification',NotificationViewSet)

urlpatterns=[
    path('',include(router.urls)),
]


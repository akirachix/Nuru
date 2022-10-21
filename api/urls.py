from django.urls import include ,path
from rest_framework import routers
from .views import MotherViewSet,InformationViewSet,NotificationViewSet


router =routers.DefaultRouter()
router.register(r'mother',MotherViewSet),
router.register(r'Information',InformationViewSet)
router.register(r'Notification',NotificationViewSet)



urlpatterns=[
    path('',include(router.urls)),
]


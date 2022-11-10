from django.urls import include ,path
from rest_framework import routers
from .views import InformationViewSet,NotificationViewSet, UsersViewSet,MessageViewSet


router =routers.DefaultRouter()
router.register(r'Users',UsersViewSet),
router.register(r'Information',InformationViewSet)
router.register(r'Notification',NotificationViewSet)
router.register(r'Message',MessageViewSet)


urlpatterns=[
    path('',include(router.urls)),
]


from django.urls import include ,path
from rest_framework import routers
from .views import InformationViewSet,NotificationViewSet, UsersViewSet,MessageViewSet,Contact_numberViewSet


router =routers.DefaultRouter()
router.register(r'Users',UsersViewSet),
router.register(r'Information',InformationViewSet)
router.register(r'Notification',NotificationViewSet)
router.register(r'Message',MessageViewSet)
router.register(r'Contact_number',Contact_numberViewSet)



urlpatterns=[
    path('',include(router.urls)),
]


from django.urls import include ,path
from rest_framework import routers
from .views import InformationViewSet, LoginView,NotificationViewSet,UsersViewSet,RegisterView




router =routers.DefaultRouter()
router.register(r'Users',UsersViewSet),
router.register(r'Information',InformationViewSet)
router.register(r'Notification',NotificationViewSet)


urlpatterns=[
    path('',include(router.urls)),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path("login",LoginView.as_view()),
    
]


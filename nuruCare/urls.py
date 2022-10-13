from django.contrib import admin
from django.urls import path

from nuru.views import contact_upload

urlpatterns =[
    path('admin/', admin.site.urls),
    path('upload_csv/', contact_upload, name="contact_upload"),
]
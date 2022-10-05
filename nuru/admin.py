from django.contrib import admin

from nuru.models import Information, Mother, Notification

# Register your models here.
class MotherAdmin(admin.ModelAdmin):
    list_display= ('first_name','last_name')
    search_fields = ('first_name', 'phone_number')

admin.site.register(Mother, MotherAdmin)

class InformationAdmin(admin.ModelAdmin):
    list_display= ('neonatal_information','clinical_information')
    search_fields = ('neonatal_information', 'clinical_information')

admin.site.register(Information, InformationAdmin)

class NotificationAdmin(admin.ModelAdmin):
    list_display= ('message','title','date_time')
    search_fields = ('message','title')

admin.site.register(Notification, NotificationAdmin)
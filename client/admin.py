from django.contrib import admin
from client.models import contactEnquiry

class clientAdmin(admin.ModelAdmin):
    list_display=('name','Email','message')


admin.site.register(contactEnquiry,clientAdmin)


# Register your models here.

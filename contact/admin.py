from django.contrib import admin
from  contact.models import contact

class contactsAdmin(admin.ModelAdmin):
    list_display=('Name','Post','Email','PhoneNo','Birthday','Location','Description')


admin.site.register(contact,contactsAdmin)



# Register your models here.

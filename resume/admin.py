from django.contrib import admin
from  resume.models import resume

class resumeAdmin(admin.ModelAdmin):
    list_display=('schooling','schooling_date','schooling_experiences','post','TimeLapse','Experience')


admin.site.register(resume,resumeAdmin)

# Register your models here.

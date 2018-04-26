from django.contrib import admin
from .models import Project

# Register your models here


class ProjectAdmin(admin.ModelAdmin):
    fields = ('sponsor', 'title', 'link', 'amount', 'deadline', 'synopsis', 'active')
    list_display = ('sponsor', 'title', 'link', 'amount', 'deadline', 'synopsis', 'active')


admin.site.site_header = 'Database Edit'
admin.site.register(Project, ProjectAdmin)

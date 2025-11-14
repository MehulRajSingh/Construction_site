# from django.contrib import admin
# from .models import Project, Contact

# admin.site.register(Project)
# admin.site.register(Contact)

from django.contrib import admin
from .models import Project, Contact

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'client_name', 'location', 'budget', 'status', 'start_date', 'end_date')
    list_filter = ('status', 'start_date')
    search_fields = ('name', 'client_name', 'location')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'project_type', 'created_at')
    list_filter = ('project_type', 'created_at')
    search_fields = ('name', 'email', 'project_type')

from django.contrib import admin

from models import Maintenance, MaintenanceFilter

class MaintenanceFilterInline(admin.TabularInline):
    model = MaintenanceFilter

class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'end_time', 'enabled')
    list_filter = ('start_time', 'end_time', 'enabled')
    list_editable = ('enabled',)
    inlines = (MaintenanceFilterInline,)
    
admin.site.register(Maintenance, MaintenanceAdmin)
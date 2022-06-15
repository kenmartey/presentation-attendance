from django.contrib import admin

# Register your models here.

from .models import PresentationAttendance


class PresentationAttendanceAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'presentation',
        'created_date', 'modified'
    )
    readonly_fields = ['created_date', 'modified']


admin.site.register(PresentationAttendance, PresentationAttendanceAdmin)

from django.contrib import admin

from .models import Attendee


class AttendeeAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'company',
        'created_date', 'modified'
    )
    readonly_fields = ['created_date', 'modified']


admin.site.register(Attendee, AttendeeAdmin)

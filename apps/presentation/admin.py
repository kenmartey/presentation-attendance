from django.contrib import admin
from .models import Presentation


class PresentationAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'presentation', 'room',
        'created_date', 'modified'
    )
    readonly_fields = ['created_date', 'modified']


admin.site.register(Presentation, PresentationAdmin)

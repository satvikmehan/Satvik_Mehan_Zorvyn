from django.contrib import admin
from .models import Record

class RecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'amount', 'type', 'category', 'date')
    list_filter = ('type', 'category')

admin.site.register(Record, RecordAdmin)
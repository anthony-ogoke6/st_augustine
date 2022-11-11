from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin





class CelebrationAdmin(SummernoteModelAdmin):
    list_display = ['title', 'event_start_date', 'event_end_date',  'slug', 'status', 'created', 'updated']
    list_filter = ('status', 'created', 'updated', 'event_start_date')
    summernote_fields = ('body',)
    prepopulated_fields = {'slug':('title',)}
    list_editable = ('status',)
    date_hierarchy = ('created')


admin.site.register(Celebration, CelebrationAdmin)
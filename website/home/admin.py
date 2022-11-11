from django.contrib import admin
from .models import *
from  embed_video.admin  import  AdminVideoMixin
from .models  import  AdvertVideo
from django_summernote.admin import SummernoteModelAdmin





class EventAdmin(SummernoteModelAdmin):
    list_display = ['title', 'event_start_date', 'event_end_date', 'event_type', 'slug', 'status', 'created', 'updated']
    list_filter = ('status', 'created', 'updated', 'event_start_date')
    summernote_fields = ('body',)
    prepopulated_fields = {'slug':('title',)}
    list_editable = ('status',)
    date_hierarchy = ('created')



class  AdvertVideoAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

    
admin.site.register(Event, EventAdmin)
admin.site.register(HomeImages)

admin.site.register(AdvertVideo, AdvertVideoAdmin)
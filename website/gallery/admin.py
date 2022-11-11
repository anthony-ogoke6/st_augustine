from django.contrib import admin
from .models import *
from  embed_video.admin  import  AdminVideoMixin
from django_summernote.admin import SummernoteModelAdmin




class GalleryAdmin(SummernoteModelAdmin):
    list_display = ['title', 'created', 'updated']
    list_filter = ('title', 'created', 'updated')
    summernote_fields = ('body',)
    date_hierarchy = ('created')



class  AdvertVideoAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

    
admin.site.register(Gallery, GalleryAdmin)

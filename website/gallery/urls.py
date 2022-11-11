from django.urls import path, re_path


from . import views

app_name = 'gallery'
urlpatterns = [
    path('', views.gallery, name='gallery'),
    re_path(r'gallery_detail/(?P<id>\d+)/(?P<slug>[\w-]+)/$', views.gallery_detail, name="gallery_detail"),
]
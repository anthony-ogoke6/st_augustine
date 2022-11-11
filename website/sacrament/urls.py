from django.urls import path, re_path


from . import views

app_name = 'sacrament'
urlpatterns = [
    path('', views.sacrament, name='sacrament'),
    # path('events/', views.events, name='events'),
    # re_path(r'event_detail/(?P<id>\d+)/(?P<slug>[\w-]+)/$', views.event_detail, name="event_detail"),
]
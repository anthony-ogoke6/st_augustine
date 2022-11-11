from django.urls import path, re_path


from . import views

app_name = 'contact'
urlpatterns = [
    path('', views.contact, name='contact'),
    path('email_list', views.email_list, name='email_list'),
    # path('events/', views.events, name='events'),
    # re_path(r'event_detail/(?P<id>\d+)/(?P<slug>[\w-]+)/$', views.event_detail, name="event_detail"),
]
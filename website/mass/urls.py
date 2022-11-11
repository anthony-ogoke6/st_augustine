from django.urls import path, re_path


from . import views

app_name = 'mass'

urlpatterns = [
    path('', views.mass, name='mass'),
    re_path(r'mass_details/(?P<id>\d+)/(?P<slug>[\w-]+)/$', views.mass_details, name="mass_details"),
]
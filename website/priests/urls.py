from django.urls import path, re_path


from . import views

app_name = 'priests'
urlpatterns = [
    path('', views.priests, name='priests'),
    re_path(r'priest_details/(?P<id>\d+)/(?P<slug>[\w-]+)/$', views.priest_details, name="priest_details"),
]
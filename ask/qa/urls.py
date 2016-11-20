from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<num>\d+)/$', views.test),
]

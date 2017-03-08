from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^savelist/$', views.save_list),
]
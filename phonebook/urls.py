from django.conf.urls import url
from django.contrib import admin
from . import views
from .views import IndexView, ContactListView

app_name = 'phonebook'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^contact$', views.contact_create, name="contact_create"),
    url(r'^contact/(?P<pk>\d+)/update/$', views.contact_update, name='contact_update'),
    url(r'^contact/(?P<pk>\d+)/delete/$', views.contact_delete, name='contact_delete'),
    url(r'^contacts$', ContactListView.as_view(), name='contacts'),
]

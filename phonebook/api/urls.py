from django.conf.urls import url
from django.contrib import admin
from . import views
from .views import (
    ContactCreteAPIView,
    ContactListAPIView,
    ContactRetrieveAPIView,
    ContactDeleteAPIView,
    ContactUpdateAPIView
)
# from .views import IndexView, ContactListView

app_name = 'api'

urlpatterns = [
    url(r'^create$', ContactCreteAPIView.as_view(), name="create"),
    url(r'^$', ContactListAPIView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', ContactRetrieveAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', ContactUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', ContactDeleteAPIView.as_view(), name='delete'),
    # url(r'^contacts$', ContactListView.as_view(), name='contacts'),
]

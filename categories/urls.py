from unicodedata import category
from django.conf.urls import url
from .import views
from django.urls import path
from categories.views import CategoryUpdate, CategoryDelete

app_name = 'categories'

urlpatterns = [
    url(r'^$', views.category_list, name='list'),
    url(r'^create/$', views.category_create, name='create'),
    url(r'^edit/(?P<pk>\d+)$', CategoryUpdate.as_view(), name='edit'),
    url(r'^delete/(?P<pk>\d+)$', CategoryDelete.as_view(), name='delete'),
]

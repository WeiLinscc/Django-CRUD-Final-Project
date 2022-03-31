import imp
from django.conf.urls import url, include
from .import views
from products.views import ProductUpdate, ProductDelete
app_name = 'products'

urlpatterns = [
    url(r'^$', views.product_list, name='list'),
    url(r'^create/$', views.product_create, name='create'),
    url(r'^edit/(?P<pk>\d+)$', ProductUpdate.as_view(), name='edit'),
    url(r'^delete/(?P<pk>\d+)$', ProductDelete.as_view(), name='delete'),
]
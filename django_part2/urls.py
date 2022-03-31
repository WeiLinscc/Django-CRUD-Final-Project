from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from products import views as product_views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^categories/', include('categories.urls')),
    url(r'^products/', include('products.urls')),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^$', product_views.product_list, name='home'),
]

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
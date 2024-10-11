from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='eng/', permanent=False)),
    path('ru/', include('catalog.urls')),
    path('eng/', include('catalog_eng.urls', namespace='eng')),
    path('custom_admin/', include('custom_admin.urls', namespace='c_admin')),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

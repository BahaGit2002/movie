from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('main.urls')),
    path('api/', include('main.api_urls')),
    path('api_register/', include('accounts.api_urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('accounts/', include('accounts.urls')),
    path('api/auth/', include('djoser.urls')),
    path('api/auth-token/', include('djoser.urls.authtoken')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


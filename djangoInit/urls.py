from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.authtoken.views import obtain_auth_token

from djangoInit import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/token/', obtain_auth_token, name='token'),
    path('adminfes/', include('adminFES.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

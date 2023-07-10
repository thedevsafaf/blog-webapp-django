from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('articles.urls')),


    path('media/(P<path>)', serve,
         {'document_root': settings.MEDIA_ROOT}),
    path('static/(<path>)', serve,
         {'document_root': settings.STATIC_FILE_ROOT}),
]

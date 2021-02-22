from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog_main.urls')),
    url(r'', include('panel.urls')),
    url(r'', include('authenticate.urls')),
    url(r'', include('miscellaneous.urls')),
]   

urlpatterns += static ( 
    settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static ( 
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
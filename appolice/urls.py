
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path 
from complaints.views import home, register, track, emergency, complaints_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('register/', register),
    path('track/', track),
    path('emergency/', emergency),
    path('complaints/', complaints_list),
]


urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
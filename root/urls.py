
from django.contrib import admin
from django.urls import path, include
from main.views import custom_404_view


urlpatterns = [
    path('login/', admin.site.urls),
    path('weather/', include('main.urls')),
]

handler404 = custom_404_view
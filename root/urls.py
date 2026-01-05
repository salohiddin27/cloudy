
from django.contrib import admin
from django.urls import path, include

from main import views

urlpatterns = [
    path('', views.custom_404_view),
    path('login/', admin.site.urls),
    path('weather/', include('main.urls')),
]

handler404 = views.custom_404_view
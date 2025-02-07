from django.contrib import admin
from django.urls import path
from .api import api
from music import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
    path('', views.index, name='home'),
    path('success/', views.success_view, name='success'),  # Добавьте этот маршрут
]

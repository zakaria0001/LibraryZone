from django.urls import path

from . import views
urlpatterns = [
    path('', views.api, name='api'),
    path('dashboard/', views.dashboard, name='dashboard'),
]

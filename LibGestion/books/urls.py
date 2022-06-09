from django.urls import path,include

from . import views
urlpatterns = [
    path('', views.api, name='api'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('accounts/', include('allauth.urls')),
    path('ConnectionAuth/',  views.ConnectionAuth, name='ConnectionAuth'),

]

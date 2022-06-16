from django.urls import path, re_path

from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('checkout/', views.checkout, name='checkout'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('Auths/', views.Auths, name='Auths'),
    path('LikedBooks/', views.LikedBooks, name='LikedBooks'),
    path('contact/', views.FeedBacks, name='FeedBack'),
]

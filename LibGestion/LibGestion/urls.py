from django.contrib import admin
from django.urls import path,include
from books.views import api,dashboard,login,ConnectionAuth,Signup
from django.contrib.auth import views as auth_views
from books import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api, name='api'),
    path('dashboard/', dashboard, name='dashboard'),
    path('accounts/', include('allauth.urls')),
    path('Signup/', Signup , name='Signup'),
    path('ConnectionAuth/',  ConnectionAuth, name='ConnectionAuth'),

]

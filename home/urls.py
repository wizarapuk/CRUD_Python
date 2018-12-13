from django.urls import path
from .views import home, my_logout
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', home, name='home'),
    path('logout', my_logout, name='logout'),

]
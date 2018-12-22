from django.urls import path
from .views import home, my_logout
from clientes.views import person_list
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', person_list, name='person_list'),
    path('logout', my_logout, name='logout'),

]
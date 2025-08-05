from django.urls import path
from . import views as this_is_portal

urlpatterns = [
    path('',this_is_portal.home, name='home'),
    path('read/',this_is_portal.read, name='read'),
]
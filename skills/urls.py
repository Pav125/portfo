from django.urls import path
from . import views

app_name = 'skills'

urlpatterns = [
    path('', views.profile_view, name = 'home'),
]
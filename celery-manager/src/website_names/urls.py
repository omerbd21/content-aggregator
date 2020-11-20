from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_website_names, name='get_website_names'),
]

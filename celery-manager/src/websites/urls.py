from django.urls import path
from . import views

urlpatterns = [
    path('<website_name>', views.get_website, name='get_website'),
]

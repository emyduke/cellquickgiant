from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import *


urlpatterns = [
    path('', index, name="home"),
    path('sales/', sales, name="sales"),
    path('repairs/', repairs, name="repairs"),
    path('about/', about, name="about"),
    path('cctv-installations', cctv_installations, name="cctv-installations"),
    path('contact-us', contact_us, name="contact-us"),
]
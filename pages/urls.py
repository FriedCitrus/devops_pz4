from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("extra/", views.extra, name="extra"),
    path("phantasm/", views.phantasm, name="phantasm"),
]
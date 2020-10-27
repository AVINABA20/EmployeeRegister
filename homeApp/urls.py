from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("goregister/", views.goregister, name="goregister"),
    path("goupdate", views.goupdate, name="goupdate"),
    path("gosearch", views.gosearch, name="gosearch"),
    path("godelete", views.godelete, name="godelete"),
]
from django.urls import path, include
from . import views

urlpatterns = [
    path("register", views.register, name="register"),
    path("register/", views.register, name="register"),
    path("doregister", views.doregister, name="doregister"),
    path("register/doregister", views.doregister, name="doregister"),
    path("gohome", views.gohome, name="gohome"),
    path("register/gohome", views.gohome, name="gohome"),
]
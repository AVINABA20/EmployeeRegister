from django.urls import path, include
from . import views

urlpatterns = [
    path('delete', views.delete, name="delete"),
    path('delete/', views.delete, name="delete"),
    path("gohome", views.gohome, name="gohome"),
    path("dodelete", views.dodelete, name="dodelete"),
    path("delete/dodelete", views.dodelete, name="dodelete"),
    path("delete/gohome", views.gohome, name="gohome"),
]
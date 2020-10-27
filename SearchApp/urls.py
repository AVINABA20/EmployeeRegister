from django.urls import path, include
from . import views

urlpatterns = [
    path('search', views.search, name="search"),
    path("gohome", views.gohome, name="gohome"),
    path("gosearchbyname", views.gosearchbyname, name="gosearchbyname"),
    path("gosearchbyempid", views.gosearchbyempid, name="gosearchbyempid"),
    path("gosearchbyage", views.gosearchbyage, name="gosearchbyage"),
    path("searchforname", views.searchforname, name="searchforname"),
    path("searchforempid", views.searchforempid, name="searchforempid"),
    path("searchforage", views.searchforage, name="searchforage"),
]
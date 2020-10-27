from django.urls import path, include
from . import views

urlpatterns = [
    path('update', views.update, name="update"),
    path("gohome", views.gohome, name="gohome"),
    path("empid_for_update", views.empid_for_update, name="empid_for_update"),
    path("changeAddress", views.changeAddress, name="changeAddress"),
    path("changeDob", views.changeDob, name="changeDob"),
    path("changeMob", views.changeMob, name="changeMob"),
    path("doUpdateAddress", views.doUpdateAddress, name="doUpdateAddress"),
    path("doUpdateDob", views.doUpdateDob, name="doUpdateDob"),
    path("doUpdateMob", views.doUpdateMob, name="doUpdateMob"),

]
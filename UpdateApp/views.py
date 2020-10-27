from django.shortcuts import render, redirect
from homeApp.models import Employee
import sqlite3

# Create your views here.
def update(request):
    return render(request, "empidsearchforupdate.html")

def gohome(request):
    return redirect("home")

def empid_for_update(request):
    global empid_search
    empid_search = request.POST["searchempid"]
    if Employee.objects.filter(employee_id= empid_search).exists():
        update_emp = Employee.objects.filter(employee_id= empid_search)
        return render(request, "update.html", {"datas":update_emp})
    else:
        message = "No Data Available"
        return render(request, "feedback.html", {"message":message})

def changeAddress(request):
    return render(request, "updateaddress.html")

def changeDob(request):
    return render(request, "updatedob.html")

def changeMob(request):
    return render(request, "updatemob.html")

def doUpdateAddress(request):
    cngaddress = request.POST["new_address"]
    emp = Employee.objects.get(employee_id= empid_search)
    emp.address = cngaddress
    emp.save()
    emp_data = Employee.objects.filter(employee_id= empid_search)
    return render(request, "update.html", {"datas":emp_data})

def doUpdateDob(request):
    cngDay = request.POST["Day"]
    cngMonth = request.POST["Month"]
    cngYear = request.POST["Year"]
    emp = Employee.objects.get(employee_id= empid_search)
    emp.dobDay = cngDay
    emp.dobMon = cngMonth
    emp.dobYear = cngYear
    emp.save()
    emp_data = Employee.objects.filter(employee_id= empid_search)
    return render(request, "update.html", {"datas":emp_data})

def doUpdateMob(request):
    cngMob = request.POST["new_mob"]
    emp = Employee.objects.get(employee_id= empid_search)
    emp.mobile_no = cngMob
    emp.save()
    emp_data = Employee.objects.filter(employee_id= empid_search)
    return render(request, "update.html", {"datas":emp_data})
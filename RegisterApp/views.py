from django.shortcuts import render,redirect
from homeApp.models import Employee
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def register(request):
    return render(request, "register.html")

def gohome(request):
    return redirect("home")

def doregister(request):

    given_id = request.POST["empid"]
    given_name = request.POST["empname"]
    given_addrs = request.POST["addrs"]
    given_dob_day = request.POST["DOBDay"]
    given_dob_mon = request.POST["DOBMonth"]
    given_dob_year = request.POST["DOBYear"] 
    given_mob = request.POST["mob"]

    
    if Employee.objects.filter(employee_id = given_id).exists():
        message = "Assosiate with this Employee ID already registerd."
        return render(request, "feedback.html", {"message":message})

    elif given_dob_day == "0" or given_dob_mon == "0" or given_dob_year == "0":
        message = "Enter the Date Properly"
        return render(request, "feedback.html", {"message":message})

    else:
        emp = Employee()
        emp.employee_id = int(given_id)
        emp.employee_name = given_name.upper()
        emp.address = given_addrs
        emp.dobDay = int(given_dob_day)
        emp.dobMon = given_dob_mon
        emp.dobYear = int(given_dob_year)
        emp.mobile_no = int(given_mob)
        emp.save()

        message = "Succesfully Registered"

        return render(request, "feedback.html", {"message": message})
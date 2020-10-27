from django.shortcuts import render, redirect
from homeApp.models import Employee
import datetime

# Create your views here.
def search(request):
    return render(request, "search.html")

def gohome(request):
    return redirect("home")

def gosearchbyname(request):
    return render(request, "searchbyname.html")

def gosearchbyempid(request):
    return render(request, "searchbyempid.html")

def gosearchbyage(request):
    return render(request, "searchbyage.html")

def searchforname(request):
    
    name_search = request.POST["searchname"]

    if Employee.objects.filter(employee_name= name_search.upper()).exists():
        empdata1 = Employee.objects.filter(employee_name= name_search.upper())

        return render (request, "searchresult.html", {"results":empdata1})
    else:
        message = "No Data Available"
        return render(request, "feedback.html", {"message": message})

def searchforempid(request):
    empid_search = int(request.POST["searchempid"])
    if Employee.objects.filter(employee_id= empid_search).exists():
        empdata2 = Employee.objects.filter(employee_id = empid_search)

        return render (request, "searchresult.html", {"results": empdata2})
    
    else: 
        message = "No Data Available"
        return render(request, "feedback.html", {"message": message})

def searchforage(request):
    given_age = int(request.POST["searchage"])
    recd_year = datetime.datetime.now().year - given_age
    if Employee.objects.filter(dobYear= recd_year).exists():
    
        all_entries = Employee.objects.filter(dobYear= recd_year)

        return render(request, "searchresult.html", {"results": all_entries})
    else:
        message = "No Data Available"
        return render(request, "feedback.html", {"message":message})



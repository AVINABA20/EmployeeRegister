from django.shortcuts import render, redirect
from homeApp.models import Employee

# Create your views here.
def delete(request):
    return render(request, "delete.html")

def gohome(request):
    return redirect("home")

def dodelete(request):
    del_emp = request.POST["delempid"]
    if Employee.objects.filter(employee_id= del_emp).exists():
        del_data = Employee.objects.filter(employee_id= del_emp)
        
        Employee.objects.filter(employee_id= del_emp).delete()
        
        message = "Succesfully Deleted."
        return render(request, "feedback.html", {"message":message})
    else:
        message = "No Data Available"
        return render(request, "feedback.html", {"message":message})
from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, "index.html")

def goregister(request):
    return redirect("register")

def goupdate(request):
    return redirect("update")

def gosearch(request):
    return redirect("search")

def godelete(request):
    return redirect("delete")


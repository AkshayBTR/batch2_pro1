from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1>Welcome to Homepage</h1>")

def demo1(request):
    return render(request,"sample.html")

def demo2(request):
    return render(request,"myapp/sample1.html")

def demo3(request):
    return render(request,"sample2.html")

def demo4(request):
    return render(request,"jinja_demo.html",{'name':["Ramesh","Suresh"],'food':"lunch?"})

def demo5(request):
    fruit=['apple','banana','orange','mango']
    return render(request,"jinja_demo1.html",context={'fruits':fruit})
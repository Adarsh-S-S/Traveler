from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from home.models import TourPackage



def package(request):
    id=request.GET["id"]
    data=TourPackage.objects.get(id=id)
    return render(request,"package.html",{"pro":data})
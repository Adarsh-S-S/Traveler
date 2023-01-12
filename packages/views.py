from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from home.models import TourPackage
from .models import Comment
from django.core.cache import cache
from django.conf import settings
from django.core.mail import send_mail
from django.http.response import JsonResponse


def package(request):
    id=request.GET["id"]
    data=TourPackage.objects.get(id=id)
    total=int(data.price)-(int(data.price)*int(data.discount)/100)
    comment=Comment.objects.filter(pro_id=id)
    if "his" in request.session:
        if id in request.session["his"]:
            request.session["his"].remove(id)
            request.session["his"].insert(0,id)
        else:
            request.session["his"].insert(0,id)
        if len(request.session["his"])>4:
            request.session["his"].pop()
        print(request.session["his"])
        recent=TourPackage.objects.filter(id__in=request.session["his"])
        print(recent)
        request.session.modified=True
        return render(request,"package.html",{"pro":data,"total":total,"comment":comment,"recent":recent})

    else:
        print("Hello")
        request.session["his"]=[id]
        print(request.session["his"])
        return render(request,"package.html",{"pro":data,"total":total,"comment":comment})



def cmt(request):
    if request.method=="POST":
        comment=request.POST["comment"]
        name=request.POST["user"]
        proid=request.POST["id"]
        mt=Comment.objects.create(cmt=comment,name=name,pro_id=proid)
        mt.save();
        return redirect("/package/?id="+proid)


def search(request):
    return render(request,"search.html")

def autosearch(request):
    if 'term' in request.GET:
        a=request.GET["term"]
        print("hii",a)
        pro=TourPackage.objects.filter(name__istartswith=a)
        print(pro)
        li=[]
        for i in pro:
            li.append(i.name)
        print(li)
        return JsonResponse(li,safe=False)

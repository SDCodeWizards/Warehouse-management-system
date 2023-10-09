from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import *
# Create your views here.

def toIndex(request):
    production_list = userInfo.objects.all()
    return render(request, 'index.html', {'production_list': production_list})


def toLogin(request):
    return render(request, 'login.html')


def Login(request):
    #if request.method == "POST":
    u = request.POST.get("username", '')
    p = request.POST.get("password", '')

    if u and p:
        c = userInfo.objects.filter(username=u, password=p).count()
        if c >= 1:
            #return toIndex(request)
            production_list = inventoryInfo.objects.all()

            return render(request, 'index.html', {'production_list': production_list})
        else:
            return HttpResponse('bad')
    else:
        return HttpResponse('bad')
    #return render(request, 'index.html')


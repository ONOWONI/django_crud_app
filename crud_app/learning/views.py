from django.shortcuts import render
from django.http import HttpResponse

from .models import Destination

# Create your views here.

def index(request):
    dests = Destination.objects.first()
    print(dests)
    context = { "dests" : dests }
    return render(request, "home.html", context)


def add(request):
    val1 = int(request.POST["num1"])
    val2 = int(request.POST["num2"])
    res = val1 + val2
    return render(request, 'add.html', {'result': res})


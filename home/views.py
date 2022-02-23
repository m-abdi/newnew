from math import gamma
import re
from django import http
from django.shortcuts import render
from .models import Data



# Create your views here.
def job(request):
    person = Data.objects.all()[0]
    return render(request,"home/first.html" , person.__dict__,
     )

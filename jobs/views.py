from django.shortcuts import render
from .models import job
# Create your views here.

def nick(request):
    jobs=job.objects
    return render(request,'jobs/nick.html',{'jobs':jobs})

def detail(request,job_id):
    jobs=job.objects.get(pk=job_id)
    return render(request,'jobs/detail.html',{'job':jobs})
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from gems.models import GemLocation


def welcome(request):
    return HttpResponse("Welcome to my page")

def gems(request):
    all_gems = GemLocation.objects.all()
    return render(request, "gems.html", {"gems": all_gems})

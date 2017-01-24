from django.shortcuts import render
from django.http import HttpResponse
import datetime

def waterkering(request):
    return render(request, 'waterkering/index.html')

# threading start | from controller.py
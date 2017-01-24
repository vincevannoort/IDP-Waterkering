from django.shortcuts import render
from django.http import HttpResponse
import datetime
import threading
import waterkering.functions.controller as controller

def waterkering(request):
    return render(request, 'waterkering/index.html')

threads = []
t = threading.Thread(target=controller.run)
print('test');
threads.append(t)
t.start()
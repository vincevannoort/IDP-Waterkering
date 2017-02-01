from django.shortcuts import render
from django.http import HttpResponse
import datetime
import threading
import waterkering.functions.controller as controller
from waterkering.functions.testing import Testing
import applicatie.settings as settings

def waterkering(request):
    return render(request, 'waterkering/index.html')

def testing(request):
    ''' Function for testing purposes, get function from url and run from the testing class '''
    Testing.test(request.GET.get('function', ''))
    return HttpResponse('')

threads = []
monitorThread = threading.Thread(target=controller.monitor)
updaterThread = threading.Thread(target=controller.updater)
threads.append(monitorThread)
threads.append(updaterThread)

for thread in threads:
    thread.start()
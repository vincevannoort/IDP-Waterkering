import datetime
import threading

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

import waterkering.functions.controller as controller
from waterkering.functions.testing import Testing
from waterkering.models import Melding
import applicatie.settings as settings

def waterkering(request):
    return render(request, 'waterkering/index.html')

def meldingen(request):
    return JsonResponse(dict(meldingen=list(Melding.objects.values('melding', 'date'))))

@csrf_exempt 
def testing(request):
    ''' Function for testing purposes, get function from url and run from the testing class '''
    Testing.test(request.GET.get('function', ''))
    return HttpResponse('')

threads = []
monitorThread = threading.Thread(target=controller.monitor)
updaterThread = threading.Thread(target=controller.updater)
copyThread = threading.Thread(target=controller.copier)
threads.append(monitorThread)
threads.append(updaterThread)
threads.append(copyThread)

for thread in threads:
    thread.start()
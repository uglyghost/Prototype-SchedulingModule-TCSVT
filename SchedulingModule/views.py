from django.shortcuts import render
from django.http import HttpResponse
import csv
# Create your views here.
from .models import *


def get(request):
    message = LinuxStat.objects.all().filter(status=0).order_by('cpu_used')
    print(message[0].host)
    with open("/home/ip.csv", 'w') as f:
        csv_write = csv.writer(f)

        for i in message:
            csv_write.writerow([i.host + ':' + str(i.port), i.check_time])
    content = {
        'message': message,
    }
    return render(request, 'messagedata.html', content)


def autoget():
    message = LinuxStat.objects.all().filter(status=0).order_by('cpu_used')
    print(message[0].host)
    with open("/home/ip.csv", 'w') as f:
        csv_write = csv.writer(f)

        for i in message:
            csv_write.writerow([i.host + ':' + str(9091), i.check_time])
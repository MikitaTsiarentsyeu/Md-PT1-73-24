from django.shortcuts import render
import datetime

def test(request):
    now = datetime.datetime.now()
    return render(request, 'test.html', {"my_time":now})
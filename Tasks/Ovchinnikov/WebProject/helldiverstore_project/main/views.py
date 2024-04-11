from django.http import HttpResponse
from django.shortcuts import render
from .models import OnSaleList, SellItemList
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound, Http404
from datetime import datetime, timezone
# Create your views here.

def index(response):
    return HttpResponse("Hi there")

def home(response):
    try:
        i = OnSaleList.objects.get(id=1)
    except ObjectDoesNotExist:
        raise Http404("Cannot find item on sale")
    
    s = i.saleEndTime - datetime.now(timezone.utc)
    return render(response, "main/home.html", {'item':i, 'saleTime':s})

def itemList(response):
    items = SellItemList.objects.all()
    return render(response, "main/shopList.html", {'items':items})
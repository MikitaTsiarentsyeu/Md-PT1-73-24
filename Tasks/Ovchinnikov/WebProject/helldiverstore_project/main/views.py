from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import OnSaleList, SellItemList, ItemReviewList
from .itemRatingForm import AddReview
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound, Http404
from datetime import datetime, timezone
# Create your views here.

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

def itemIndex(response, itemIndex):
    try:
        item = SellItemList.objects.get(id=itemIndex)
    except ObjectDoesNotExist:
        # return HttpResponseNotFound("cannot find post specified")
        raise Http404("cannot find post specified")
    
    if response.method == "POST":
        ratingForm = AddReview(response.POST)
        if ratingForm.is_valid():
            formData = ratingForm.cleaned_data["reviewRating"]
            reviewsTable = ItemReviewList()
            reviewsTable.save()
            return HttpResponseRedirect("shop/%i" %reviewsTable)
    else:
        ratingForm = AddReview()
    
    return render(response, "main/shopItem.html", {'item':item, 'form':ratingForm})
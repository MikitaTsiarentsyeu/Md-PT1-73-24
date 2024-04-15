from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import OnSaleList, SellItemList, ItemReviewList, UserList
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
        print(response.POST)
        if ratingForm.is_valid():
            reviewText = ratingForm.cleaned_data["reviewText"]
            reviewRating = ratingForm.cleaned_data["reviewRating"]
            reviewsTable = ItemReviewList(author = UserList.objects.all()[0], 
                                          item_id = itemIndex, review_text = reviewText, 
                                          rating = reviewRating, postTime = datetime.now())
            reviewsTable.save()
            return HttpResponseRedirect("/shop/%i" %itemIndex)
    else:
        ratingForm = AddReview()
    
    # add rating
    try:
        itemReviews = ItemReviewList.objects.filter(item_id = itemIndex)
        print(f"itemReviews:{itemReviews}")
    except ObjectDoesNotExist:
        # return HttpResponseNotFound("cannot find post specified")
        raise Http404("cannot find post specified")
    
    return render(response, "main/shopItem.html", {'item':item, 'form':ratingForm, 'reviews':itemReviews})
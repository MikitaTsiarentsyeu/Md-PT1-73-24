from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import OnSaleList, SellItemList, ItemReviewList, UserList
from .citeForms import AddReview
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound, Http404
from datetime import datetime, timezone
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.

def home(response):
    try:
        i = OnSaleList.objects.get(id=1)
    except ObjectDoesNotExist:
        raise Http404("Cannot find item on sale")
    sa = i.itemData.item_price * ((100 - i.savePercentage) / 100)

    s = i.saleEndTime - datetime.now(timezone.utc)
    print(f"sale price = {sa}")
    return render(response, "main/home.html", {'item':i, 'saleTime':s, 'postSalePrice:':sa,})

def itemList(response):
    items = SellItemList.objects.all()
    return render(response, "main/shopList.html", {'items':items})

def itemIndex(response, itemIndex):
    try:
        item = SellItemList.objects.get(id=itemIndex)
    except ObjectDoesNotExist:
        raise Http404("cannot find specified item")
    
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
            return redirect("/shop/%i" %itemIndex)
    else:
        ratingForm = AddReview()
    
    # add rating
    try:
        itemReviews = ItemReviewList.objects.filter(item_id = itemIndex)
        print(f"itemReviews:{itemReviews}")
    except ObjectDoesNotExist:
        # return HttpResponseNotFound("cannot find post specified")
        raise Http404("cannot find specified item review")
    
    return render(response, "main/shopItem.html", {'item':item, 'form':ratingForm, 'reviews':itemReviews})

def userRegistration(response):
    if response.method == "POST":
        print(response.POST)
        userRegistrationForm = UserCreationForm(response.POST)
        if userRegistrationForm.is_valid():
            userRegistrationForm.save()
            return redirect("/")
    else:
        userRegistrationForm = UserCreationForm()

    return render(response, "main/register.html", {"form":userRegistrationForm})

def userLogin(response):
    if response.method == "POST":
        print(response.POST)
        userAuthenticationForm = AuthenticationForm(response.POST)
        if(userAuthenticationForm.is_valid):
            #userAuthenticationForm.save()
            try:
                username = response.POST.get('username')
                password = response.POST.get('password')
                user = authenticate(username=username, password=password)

                if user is not None:
                    login(response, user)
                    response.session['user_id'] = user.id
                    print("user login successfull")
                    return redirect("/")
            except:
                print("User don't exists")
                return redirect("login")
    else:
        userAuthenticationForm = AuthenticationForm()

    return render(response, "main/login.html", {"form":userAuthenticationForm})
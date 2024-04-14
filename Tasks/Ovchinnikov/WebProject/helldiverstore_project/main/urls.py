from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("shop", views.itemList, name="shop"),
    path("shop/<int:itemIndex>", views.itemIndex, name="itemIndex"),
]
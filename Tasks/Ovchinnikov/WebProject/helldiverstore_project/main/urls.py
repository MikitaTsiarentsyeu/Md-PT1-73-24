from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("shop", views.itemList, name="shop"),
    path("shop/<int:itemIndex>", views.itemIndex, name="itemIndex"),
    path("register", views.userRegistration, name="register"),
    path("enlist", views.userLogin, name="enlist"),
    path("logout", views.logout_view, name="logout"),
]
from django.contrib import admin
from .models import UserList, SellItemList, ItemReviewList, OnSaleList
# Register your models here.
admin.site.register(UserList)
admin.site.register(SellItemList)
admin.site.register(ItemReviewList)
admin.site.register(OnSaleList)
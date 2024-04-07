from django.contrib import admin
from .models import UserList, SellItemList, ItemReviewList
# Register your models here.
admin.site.register(UserList)
admin.site.register(SellItemList)
admin.site.register(ItemReviewList)
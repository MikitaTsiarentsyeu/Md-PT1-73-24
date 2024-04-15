from django.db import models

# Create your models here.
class UserList(models.Model):
    name = models.CharField(blank= False, max_length= 100)
    email = models.EmailField(primary_key=True)
    
class SellItemList(models.Model):
    ITEM_TYPE = [('b', "bodyArmor"), ('h', "headArmor"), ('w', "primaryWeapon"), ('s', "secondaryWeapon")]

    name = models.CharField(blank= False, max_length= 100)
    description = models.TextField()
    item_type = models.CharField(choices=ITEM_TYPE, max_length=1)
    image = models.ImageField(upload_to='uploads')
    item_price = models.IntegerField(blank=False, default=0)

class ItemReviewList(models.Model):
    author = models.ForeignKey('UserList', on_delete=models.CASCADE)
    item_id = models.IntegerField(blank= False,)
    review_text = models.TextField(default="")
    rating = models.PositiveIntegerField()
    postTime = models.DateTimeField()

class OnSaleList(models.Model):
    itemData = models.ForeignKey('SellItemList', on_delete=models.CASCADE)
    savePercentage = models.PositiveIntegerField()
    saleEndTime = models.DateTimeField()
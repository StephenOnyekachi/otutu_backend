
from django.db import models
from account.models import Profile

# Create your models here.

class Items(models.Model):
    name = models.CharField(max_length=150)
    out_number = models.TextField()
    but_price = models.IntegerField(default=0)
    selling_price = models.IntegerField(default=0.0)
    des = models.TextField()
    image = models.FileField(upload_to='image')
    quantity = models.IntegerField()
    is_avaliable = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class CrediteNote(models.Model):
    price = models.IntegerField()
    quantity = models.IntegerField()
    name = models.CharField(max_length=500)
    number = models.CharField(max_length=20)
    note = models.TextField()
    date = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class SellsNote(models.Model):
    price = models.IntegerField()
    total = models.IntegerField()
    quantity = models.IntegerField()
    item = models.ForeignKey(Items, on_delete=models.CASCADE, related_name="sell_products")
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item.name


class Cart(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="user_cart")
    item = models.ForeignKey(Items, on_delete=models.CASCADE, related_name="cart_item")
    quantity = models.IntegerField()
    total = models.IntegerField(default=0)
    paid = models.BooleanField(default=False)
    suplid = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item.name


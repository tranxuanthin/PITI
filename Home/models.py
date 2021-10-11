from django.db import models

# Create your models here.
from typing import List
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver


# Create your models here.
class List(models.Model):
    name = models.CharField(max_length=200)
    discription = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=120)
    logo = models.ImageField(upload_to='customers',default='no_picture.png')
    address = models.CharField(max_length=200)
    userid = models.ForeignKey(User,on_delete=CASCADE)
    score = models.IntegerField()
    def __str__(self):
        return self.name
class Distributor(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.IntegerField(help_text='in US dollars $$$')
    description = models.CharField(max_length=500)
    quantity = models.IntegerField()
    promotion = models.FloatField(max_length=10,default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    logo = models.ImageField(default='no_picture.png')
    distributor = models.ForeignKey(Distributor,null=True,on_delete=models.SET_NULL)
    listid = models.ForeignKey(List,null=True,on_delete=models.SET_NULL)
    def __str__(self):
        a = self.name[0:10]
        return f"{a}--{self.created.strftime('%d/%m/%Y')}"
class Bill(models.Model):
    Customer = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    quantity = models.IntegerField()
    total = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.total}$--{self.created.strftime('%d/%m/%Y')}"
class BillInfo(models.Model):
    billid = models.ForeignKey(Bill, on_delete=CASCADE)
    productid = models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    quantity = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    note = models.CharField(max_length=200)
    def __str__(self):
        return f"Chi tiet HD so{self.billid}"
class Order(models.Model):
    productid = models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    Distributor = models.ForeignKey(Distributor,null=True,on_delete=models.SET_NULL)
    BillInfo = models.ForeignKey(Bill,null=True,on_delete=models.SET_NULL)
    quantity = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Đơn hàng nhập từ {self.Distributor}--{self.created.strftime('%d/%m/%Y')}"

class Test(models.Model):
    name = models.CharField(max_length=200)
    status = models.BooleanField(default=False)



def pre_save_test(sender,instance,**kwargs):
    print("running")
pre_save.connect(pre_save_test,sender=Test)

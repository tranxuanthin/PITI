from django.contrib import admin
from .models import Customer
from .models import Product,Distributor,Bill,BillInfo,Order,List

admin.site.register(Customer)
admin.site.register(Product)
# Register your models here.
admin.site.register(Distributor)
admin.site.register(Bill)
admin.site.register(Order)
admin.site.register(List)

class Filter(admin.ModelAdmin):
    list_display = ("billid","productid","quantity","created")
    list_filter = ("billid","productid","quantity","created")
admin.site.register(BillInfo,Filter)





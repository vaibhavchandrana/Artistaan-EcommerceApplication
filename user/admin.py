from django.contrib import admin
from user.models import Customer,UserOrder



class AdminCustomer(admin.ModelAdmin):
    list_display=['name','email','address']

class AdminuserOrder(admin.ModelAdmin):
    list_display=['productName','customer','order_date']



# Register your models here.
admin.site.register(Customer,AdminCustomer)
admin.site.register(UserOrder,AdminuserOrder)
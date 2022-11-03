from django.contrib import admin
from .models import Product
from .models import Category
from .models import Customer,Admin


class AdminProduct(admin.ModelAdmin):
    list_display=['name','price','category']

class AdminCategory(admin.ModelAdmin):
    list_display=['name']

class AdminCustomer(admin.ModelAdmin):
    list_display=['name','email','address']

class AdminUser(admin.ModelAdmin):
    list_display=['name','email','address']

class AdminOrder(admin.ModelAdmin):
    list_display=['product','customer','date']

class AdminuserOrder(admin.ModelAdmin):
    list_display=['productName','customer','order_date']



# Register your models here.
admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Customer,AdminCustomer)
#admin.site.register(Order,AdminOrder)
admin.site.register(Admin,AdminUser)
#admin.site.register(UserOrder,AdminuserOrder)
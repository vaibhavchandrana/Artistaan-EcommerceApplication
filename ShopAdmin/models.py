from django.db import models
import datetime
from user.models import Customer
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

    @staticmethod
    def get_all_category():
        return Category.objects.all()

    @staticmethod
    def delete_by_id(pid):
        if pid:
            record= Category.objects.filter(id=pid)
            record.delete()

    @staticmethod
    def get_cat_by_id(c_id):
        if c_id:
            return Category.objects.filter(id=c_id)
  


class Product(models.Model):
    name=models.CharField(max_length=200)
    price=models.IntegerField()
    img1=models.ImageField(null=True,blank=True)
    img2=models.ImageField(null=True,blank=True)
    img3=models.ImageField(null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    desc=models.CharField(max_length=5000,default='',null=True,blank=True)
    manufacturer=models.EmailField(blank=True)
    instock=models.IntegerField(default=0)
    
    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_prd_id(prd_id):
        if prd_id:
            return Product.objects.filter(id=prd_id)
        else:
            return Product.objects.all()
    
    @staticmethod
    def get_all_products_by_ids(ids):
        if ids:
            return Product.objects.filter(id__in=ids)
        
    @staticmethod
    def delete_by_id(pid):
        if pid:
            record= Product.objects.filter(id=pid)
            record.delete()

    @staticmethod
    def get_all_products_by_cat_id(cat_id):
        if cat_id:
            return Product.objects.filter(category=cat_id)
        else:
            return Product.objects.all()

    @staticmethod
    def get_all_products_of_admin(mail):
        return Product.objects.filter(manufacturer=mail) # return one object only




class Order(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.IntegerField()
    date=models.DateField(default=datetime.datetime.today)
    delivery_date=models.DateField(null=True,blank=True)
    address=models.CharField(max_length=100,default='',blank=True)
    phone=models.CharField(max_length=15,default='',blank=True)
    paymentMethod=models.CharField(max_length=20,default='',blank=True)
    manufacturer=models.EmailField(blank=True)
    status=models.CharField(max_length=30,default='',blank=True)

    def saveOrder(self):
        self.save()

    @staticmethod
    def get_all_order_of_admin(mail):
        return reversed(Order.objects.filter(manufacturer=mail))

    def deleteorder(id):
        record = Order.objects.get(id = id)
        record.delete()

    @staticmethod
    def get_all_ord_by_ord_id(prd_id):
        return Order.objects.filter(id=prd_id)


class Admin(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    gst=models.CharField(max_length=20,blank=True)
    password=models.CharField(max_length=500)
    address=models.CharField(max_length=500)
    
    def register(self):
        self.save()

    def isExists(self):
        if Admin.objects.filter(email=self.email):
            return True
        else:
            return False


    @staticmethod
    def get_admin_by_email(email):
        try:
            return Admin.objects.get(email=email) # return one object only
        except:
            return False

    
    @staticmethod
    def get_by_id(c_id):
            return Admin.objects.filter(id=c_id) # return one object only

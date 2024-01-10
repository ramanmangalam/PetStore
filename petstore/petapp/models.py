from django.db import models

# Create your models here.
class contact1(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField( max_length=254)
    desc=models.TextField()
    phone=models.IntegerField()

    def __str__(self):
        return self.name




class product1(models.Model):
    pid=models.AutoField
    pname=models.CharField(max_length=50)
    category=models.CharField(max_length=50,default=" ")
    subcategory=models.CharField(max_length=50,default=" ")
    price=models.IntegerField(default=0)
    desc=models.CharField (max_length=300)
    image=models.ImageField( upload_to='images/image', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.pname

class orders(models.Model):
    order_ID = models.AutoField
    item_json = models.CharField(max_length=100)
    amount = models.IntegerField
    name = models.CharField(max_length=100)
    email = models.EmailField
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.IntegerField
    payment_details = models.CharField(max_length=100)
    phone_number = models.IntegerField
    def _str_(self):
        return self.name
    
class orderupdate(models.Model):
    updateID = models.AutoField
    oid = models.IntegerField()
    update_desc = models.CharField(max_length = 300)
    delivered = models.BooleanField()
    timestamp = models.DateField()

    def _str_(self):
        return self.oid




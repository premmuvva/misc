from django.db import models
from accounts.models import UserProfile

# Create your models here.

class Suppliers(models.Model):
    supplier_code=models.IntegerField(primary_key=True)
    supplier_name=models.CharField(max_length=100, default='')

    def __str__(self):
        return self.supplier_name

class Ref_Frequencies(models.Model):
    frequency_code=models.IntegerField(primary_key=True)
    frequency_description=models.TextField(default='', blank=True)

    def __str__(self):
        return self.frequency_description

class Magazines(models.Model):
    magazine_id=models.IntegerField(primary_key=True)
    magazine_name=models.CharField(max_length=100, default='')
    publication_frequency_code=models.ForeignKey(Ref_Frequencies, on_delete=models.CASCADE)
    price=models.IntegerField()

    def __str__(self):
        return self.magazine_name

class Publisher(models.Model):
    magazine_id=models.ForeignKey(Magazines, on_delete=models.CASCADE)
    publisher_name=models.CharField(max_length=100, default='')
    year_of_publication=models.DateField(blank=True,null=True)

    def __str__(self):
        return self.publisher_name

class Customers(models.Model):
    customer_id=models.ForeignKey(UserProfile, on_delete=models.CASCADE,null=True)
    #newsagent_id=models.IntegerField()
    # customer_name=models.CharField(max_length=20, default='')
    customer_address=models.TextField(default='', blank=True)
    customer_phone=models.IntegerField(default=0,blank=True)
    customer_email=models.EmailField(max_length=70, null=True, blank=True, unique=True)
    other_customer_details=models.TextField(default='', blank=True)

    def __int__(self):
        return self.customer_id

class Customer_Invoices(models.Model):
    invoice_id=models.IntegerField(primary_key=True)
    customer_id=models.ForeignKey(Customers, on_delete=models.CASCADE,default=-1)
    date_of_invoice=models.DateTimeField()
    invoice_amount=models.IntegerField()
    other_invoice_details=models.TextField(default='', blank=True)

    def __str__(self):
        return self.invoice_id

class Invoice_Line_Items(models.Model):

    class Meta:
        unique_together = (('invoice_id', 'item_number'),)

    invoice_id=models.ForeignKey(Customer_Invoices, on_delete=models.CASCADE)
    item_number=models.IntegerField(primary_key=True)
    customer_id=models.IntegerField()
    magazine_id=models.IntegerField()
    date_magazine_delivered=models.DateTimeField( blank=True)

    def __str__(self):
        return self.invoice_id


class Customer_Subscriptions(models.Model):

    class Meta:
        unique_together = (('customer_id', 'magazine_id'),)

    customer_id=models.ForeignKey(Customers, on_delete=models.CASCADE)
    magazine_id=models.ForeignKey(Magazines, on_delete=models.CASCADE)
    date_subscription_started=models.DateTimeField()
    date_subscription_ended=models.DateTimeField()

    def __str__(self):
        return self.customer_id


class Magazine_Suppliers(models.Model):

    class Meta:
        unique_together = (('magazine_id', 'supplier_code'),)

    magazine_id=models.ForeignKey(Magazines, on_delete=models.CASCADE)
    supplier_code=models.ForeignKey(Suppliers, on_delete=models.CASCADE)
    supplied_from_date=models.DateTimeField()
    supplied_to_date=models.DateTimeField()

    def __int__(self):
        return self.magazine_id


















#     user= models.OneToOneField(User, on_delete=models.CASCADE)
#     description = models.CharField(max_length=100, default='')
#     city = models.CharField(max_length=100,  default='')
#     website = models.URLField(default='')
#     phone = models.IntegerField(default=0)

#     def __str__(self):
#         return self.user.username

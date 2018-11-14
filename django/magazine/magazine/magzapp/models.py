from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    dob = models.DateField(default='2018-09-08')
    country = models.CharField(max_length=15, default='India')
    email = models.EmailField(max_length=30, unique=True)
    photo = models.FileField()
    phone_number = models.IntegerField(default=0)
    user_address = models.CharField(max_length=200,default='')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    due= models.IntegerField(default=0)

    def __str__(self):
        return self.email


class Supplier(models.Model):
    supplier_name = models.CharField(unique=True, max_length=50)
    def __str__(self):
        return self.supplier_name


class ReferenceFrequency(models.Model):
    reference_code = models.CharField(primary_key=True, max_length=100)
    ref_desciption = models.CharField(max_length=15, blank=True,null=True)
    def __str__(self):
        return self.reference_code


class Magazine(models.Model):
    magazine_name = models.CharField(max_length=100, unique=True)
    price = models.IntegerField(default=199)
    supplier_id = models.ForeignKey('Supplier', on_delete=models.CASCADE)
    magazine_cover = models.FileField()
    reference_code = models.ForeignKey('ReferenceFrequency', on_delete=models.CASCADE)
    desc=models.TextField(default='default')

    def __str__(self):
        return self.magazine_name


class UserSubscription(models.Model):
    user_id = models.ForeignKey('Users', on_delete=models.CASCADE)
    magazine_id = models.ForeignKey('Magazine', on_delete=models.CASCADE)
    date_subscription_started = models.DateTimeField()
    date_subscription_ended = models.DateTimeField()


class UserInvoice(models.Model):
    invoice_number = models.CharField(max_length=100, primary_key=True)
    customer_id = models.ForeignKey('Users', on_delete=models.CASCADE)
    date_of_invoice = models.DateField()
    invoice_amount = models.IntegerField()

    def __str__(self):
        return self.invoice_number


class InvoiceLineItems(models.Model):
    invoice_number = models.ForeignKey('UserInvoice', on_delete=models.CASCADE)
    item_number = models.IntegerField()
    customer_id = models.ForeignKey('Users', on_delete=models.CASCADE)
    magazine_id = models.ForeignKey('Magazine', on_delete=models.CASCADE)
    delivery_date = models.ForeignKey(
        'UserSubscription', on_delete=models.CASCADE)


class MagazineStatus(models.Model):
    magazine_name = models.ForeignKey('Magazine', on_delete=models.CASCADE)
    user = models.ForeignKey('Users', on_delete=models.CASCADE)
    status = models.IntegerField(default=1)
    class Meta:
        unique_together = ('magazine_name', 'user',)

    def __str__(self):
        return self.status

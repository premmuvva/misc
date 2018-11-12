from django.contrib import admin
from magazine_database.models import * 

# # Register your models here.
# class UserProfileAdmin(admin.ModelAdmin):
#     list_display=('user','user_info','city','website','phone')

#     def user_info(self,obj):
#         return obj.description
#     user_info.short_description='Info'
# admin.site.register(UserProfile,UserProfileAdmin)
# admin.site.site_header='Admin'


# class Suppliers(admin.ModelAdmin):
#     list_display=('supplier_code','supplier_name')

class SuppliersAdmin(admin.ModelAdmin):
    list_display=('supplier_name','supplier_code')
class PublisherAdmin(admin.ModelAdmin):
    list_display=('publisher_name',)
admin.site.register(Suppliers,SuppliersAdmin)
class Ref_FrequenciesAdmin(admin.ModelAdmin):
    list_display=('frequency_code',)
class Invoice_Line_ItemsAdmin(admin.ModelAdmin):
    list_display=('invoice_id',)
class CustomersAdmin(admin.ModelAdmin):
    list_display=('customer_id',)
class Customer_InvoicesAdmin(admin.ModelAdmin):
    list_display=('invoice_id',)
class Customer_SubscriptionsAdmin(admin.ModelAdmin):
    list_display=('customer_id',)
class MagazinesAdmin(admin.ModelAdmin):
    list_display=('magazine_name',)
class Magazine_SuppliersAdmin(admin.ModelAdmin):
    list_display=('magazine_id',)
admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Ref_Frequencies,Ref_FrequenciesAdmin)
admin.site.register(Invoice_Line_Items,Invoice_Line_ItemsAdmin)
admin.site.register(Customers,CustomersAdmin)
admin.site.register(Customer_Invoices,Customer_InvoicesAdmin)
admin.site.register(Customer_Subscriptions,Customer_SubscriptionsAdmin)
admin.site.register(Magazines,MagazinesAdmin)
admin.site.register(Magazine_Suppliers,Magazine_SuppliersAdmin)
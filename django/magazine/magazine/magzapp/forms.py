from django import forms
from .models import *

from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm,UserChangeForm

class EditProfileForm(UserChangeForm):
    class Meta:
        model = Users
        fields=(
            'email',
            'country',
            'phone_number',
            'user_address'
        )



class UserForms(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    # phone_number = forms.IntegerField()
    # user_address = forms.CharField(max_length=200)

    class Meta:
        model = Users
        fields = ('username', 'first_name', 'last_name', 'phone_number',
                  'user_address', 'email', 'dob', 'country', 'password',)


class SupplierDetails(forms.ModelForm):
    class Meta:
        model = Supplier
        exclude = []


class MagazineDetails(forms.ModelForm):
    class Meta:
        model = Magazine
        # fields = ('magazine_name', 'price')
        exclude = []




class RefernceFrequencyForm(forms.ModelForm):
	class Meta:
		model = ReferenceFrequency
		exclude = []

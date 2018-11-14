from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.http import HttpResponse
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm,UserChangeForm
import csv
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User,Permission
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,View,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin

def signupuser(request):
    if request.method == "GET":
        form = UserForms()
        return render(request, 'signup.html', {'form': form})
    if request.method == "POST":
        form = UserForms(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponse("Congrats You are a member now!!")
        else:
            return render(request, 'signup.html', {'form': form})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        user = authenticate(
            email=request.POST['eemail'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            return render(request, 'login.html', {'error': "You are not a member yet please signIn"})


@login_required
def homepage(request):

    if request.method == 'GET':
        return render(request, 'homepage.html',{'b_g':"/media/78b90a8ac172941dba527a898decb614.jpg"})

class SearchBook(ListView):
	def get(self,request):
		return render(request,'search.html')
	def post(self,request):
		search_results = Magazine.objects.filter(magazine_name__icontains=request.POST['searchme'])
		return render(request, 'search.html', {'books': search_results,'b_g':"/media/pubsofyore.jpg",'user':Users.objects.get(id=request.user.id)})

def logoutuser(request):
    logout(request)
    return redirect('loginuser')


@login_required
def change_password(request):
    if request.method =='POST':
        form=PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect ('view_profile')
        else:
            return redirect ('change_password')
    
    else:
        form = PasswordChangeForm(user=request.user)

        args= {'form' : form }
        return render(request,'change_password.html',args)

@login_required
def edit_profile(request):
    if request.method =='POST':
        form=EditProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect ('view_profile')
    else:
        form = EditProfileForm(instance=request.user)

        args= {'form' : form }
        return render(request,'edit_profile.html',args)

@login_required
def magazine_list(request):
    if request.method == 'GET':
        magazines = Magazine.objects.all()
        magazine_status = MagazineStatus.objects.all()
        return render(request, 'magazines.html', {'magazines': magazines, 'bstatus':magazine_status,'b_g':"/media/pubsofyore.jpg",'user':Users.objects.get(id=request.user.id)})


@login_required
def view_profile(request):
    if request.method == 'GET':
        return render(request, 'profile.html',{'b_g':"/media/hwehd.jpg"})


@login_required
def subscription_list(request):
    if request.method == 'GET':
        magazines = UserSubscription.objects.all()
        magazine_status = MagazineStatus.objects.all()
        return render(request, 'subscription_list.html', {'magazines': magazines, 'bstatus':magazine_status,'b_g':"/media/Ebony-Jet.jpg"})


@login_required
def cart(request):
    if request.method == 'GET':
        magazines = UserSubscription.objects.all()
        magazine_status = MagazineStatus.objects.all()
        c=0
        for b in magazine_status:
            if b.user==Users.objects.get(id=request.user.id) and b.status==2:
                c+=b.magazine_name.price
        b.user.due=c
        b.save()
        return render(request, 'cart.html', {'magazines': magazines,'total': b.user.due , 'bstatus':magazine_status,'b_g':"/media/iStock-817240836.jpg"})


# @staff_member_required
def entermagazine(request):
    if request.method == 'GET':
        magazine = MagazineDetails()
        return render(request, 'entermagzine.html', {'book': magazine,'b_g':"/media/78b90a8ac172941dba527a898decb614.jpg"})
    if request.method == "POST":
        form = MagazineDetails(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Done Magazine Updated!!")
        else:
            return render(request, 'entermagzine.html', {'book': form,'b_g':"/media/78b90a8ac172941dba527a898decb614.jpg"})


def entersupplier(request):
    if request.method == 'GET':
        supplier = SupplierDetails()
        return render(request, 'entermagzine.html', {'book': supplier,'b_g':"/media/78b90a8ac172941dba527a898decb614.jpg"})
    if request.method == "POST":
        form = SupplierDetails(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Done supplier Updated!!")
        else:
            return render(request, 'entermagzine.html', {'book': form,'b_g':"/media/78b90a8ac172941dba527a898decb614.jpg"})


def enter_reference_frequency(request):
    if request.method == 'GET':
        frequency = RefernceFrequencyForm()
        return render(request, 'entermagzine.html', {'book': frequency,'b_g':"/media/78b90a8ac172941dba527a898decb614.jpg"})
    if request.method == "POST":
        form = RefernceFrequencyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Done supplier Updated!!")
        else:
            return render(request, 'entermagzine.html', {'book': form,'b_g':"/media/78b90a8ac172941dba527a898decb614.jpg"})


def subscribe(request, mag_id):
    if MagazineStatus.objects.filter(id=mag_id, user=Users.objects.get(id=request.user.id)).exists():
        MagazineStatus.objects.get(
            id=mag_id, user=Users.objects.get(id=request.user.id)).delete()
    MagazineStatus.objects.create(user=Users.objects.get(
        id=request.user.id), magazine_name=Magazine.objects.get(id=mag_id), status='subscribed')
    return redirect('magazine_list')


def unsubscribe(request, mag_id):
    if MagazineStatus.objects.filter(id=mag_id, user=Users.objects.get(id=request.user.id)).exists():
        MagazineStatus.objects.get(
            id=mag_id, user=Users.objects.get(id=request.user.id)).delete()
    MagazineStatus.objects.create(user=Users.objects.get(
        id=request.user.id), magazine_name=Magazine.objects.get(id=mag_id), status='Unsubscribed')
    return redirect('magazine_list')

def status1(request, mag_id):
    if MagazineStatus.objects.filter(magazine_name=mag_id, user=Users.objects.get(id=request.user.id)).exists():
        MagazineStatus.objects.get(magazine_name=mag_id, user=Users.objects.get(id=request.user.id)).delete()
    MagazineStatus.objects.create(user=Users.objects.get(
        id=request.user.id), magazine_name=Magazine.objects.get(id=mag_id), status=2)
    return redirect('magazine_list')

def status2(request):
    for i in  MagazineStatus.objects.all():
        if i.status==2:
            i.status=3
            i.save()
    user=Users.objects.get(id=request.user.id)
    user.due=0
    user.save()
    return redirect('magazine_list')

def status3(request, mag_id):
    if MagazineStatus.objects.filter(magazine_name=mag_id, user=Users.objects.get(id=request.user.id)).exists():
        MagazineStatus.objects.get(magazine_name=mag_id, user=Users.objects.get(id=request.user.id)).delete()
    MagazineStatus.objects.create(user=Users.objects.get(
        id=request.user.id), magazine_name=Magazine.objects.get(id=mag_id), status=1)
    return redirect('magazine_list')

def display(request, mag_id):
    return render(request, 'mag_details.html',{'b':Magazine.objects.get(pk=mag_id),'b_g':"/media/81496ec3-b5ab-4e4c-a662-66daa33a0968.jpg"})
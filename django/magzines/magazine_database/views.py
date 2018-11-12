from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("hello!")

def magazine_list(request):
    if request.method == 'GET':
        magazines = Magazine.objects.all()
        return render(request, 'magazine_list.html')


def subscription_list(request):
	if request.method == 'GET':
		magazines = Customer_Subscriptions.get.all()
		return render(request, subscription_list.html, {'magazines': magazines})
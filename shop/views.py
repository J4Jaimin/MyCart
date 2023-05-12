from django.http import HttpResponse
from django.shortcuts import render
from shop.models import Product

# Create your views here.
def index2(request):
    args = {}
    data = Product.objects.all()
    args['data'] = data

    return render(request, 'shop/index2.html', args)

def about(request):
    return render(request, 'shop/about.html')
    # return HttpResponse("We are at about!")

def contact(request):
    return render(request, 'shop/contact.html')
    # return HttpResponse("We are at contact!")

def tracker(request):
    return render(request, 'shop/tracker.html')
    # return HttpResponse("We are at tracking system!")

def search(request):
    return render(request, 'shop/search.html')
    # return HttpResponse("We are at search!")

def productview(request):
    return render(request, 'shop/productview.html')
    # return HttpResponse("We are at product view!")

def checkout(request):
    return render(request, 'shop/checkout.html')


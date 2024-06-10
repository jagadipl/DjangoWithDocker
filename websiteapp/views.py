from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'websiteapp/index.html')
def about(request):
    return render(request,'websiteapp/about.html')
def contacte(request):
    return render(request,'websiteapp/contact.html')
def interest(request):
    return render(request,'websiteapp/interest.html')
def gallery(request):
    return render(request,'websiteapp/gallery.html')
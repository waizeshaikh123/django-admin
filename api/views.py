from django.shortcuts import render,HttpResponse
from api.models import Form
from datetime import datetime

# Create your views here.

def home(request):
    context = {
        'variable': 'This is home page but as a contet variable'
    }
    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")

def login(request):
    if request.method == 'POAT':
        name = request.POST.get['name']
        email = request.POST.get['email']
        password = request.POST.get['password']
        contact = Form(name=name, email=email, password=password, date=datetime.today())
        contact.save()
    return render(request, "login.html")
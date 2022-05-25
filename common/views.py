from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'common/signin.html')

def home(request):
    return render(request,'common/signup.html')

def home1(request):
    return render(request,'common/home.html')
# def signin(request):
#     return render(request,'common/signin.html')
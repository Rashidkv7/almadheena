from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'common/signin.html')

def home(request):
    return render(request,'common/signup.html')

# def signin(request):
#     return render(request,'common/signin.html')
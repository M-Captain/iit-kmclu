from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hi this is me")
def login(request):
    return render(request , "login.html")
def signup(request):
    return render(request , "signup.html")
from django.shortcuts import render, HttpResponse
variable = {}
# Create your views here.
def index(request):
    return HttpResponse("Hi this is me")
def login(request):
    if request.method == "POST":
        variable= request.POST
        return render(request , "login.html", variable)
    else:        
        return render(request , "login.html")
def signup(request):
    return render(request , "signup.html")
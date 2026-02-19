from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
 
def index(request):
    data = {"header": "Главная страница", "message": "Welcome to my first Django project"}
    return render(request, "index.html", context=data)

def about(request):
    return render(request, "about.html")

def contacts(request):
    return render(request, "contacts.html")

def projects(request):
    return render(request, "projects.html")

def post(request):
    userform = UserForm()
    return render(request, "post.html", {"form": userform})

def postuser(request):
    name = request.POST.get("name")
    age = request.POST.get("age")
    return HttpResponse(f"<h2>Привет, {name}, твой возраст: {age}</h2>")
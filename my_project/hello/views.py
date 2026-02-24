from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound

from .models import Person

#Main page 
def index(request):
    data = {"header": "Главная страница", "message": "Welcome to my first Django project"}
    return render(request, "index.html", context=data)

#Contacts page
def contacts(request):
    return render(request, "contacts.html")

#My project
def projects(request):
    return render(request, "projects.html")

#DB interaction
def database(request):
    people = Person.objects.all()
    return render(request, "database.html", {"people": people})

    # сохранение данных в бд
def create(request):
    if request.method == "POST":
        person = Person()
        person.name = request.POST.get("name")
        person.age = request.POST.get("age")
        person.save()
    return HttpResponseRedirect("/database")

    # изменение данных в бд
def edit(request, id):
    try:
        person = Person.objects.get(id=id)
 
        if request.method == "POST":
            person.name = request.POST.get("name")
            person.age = request.POST.get("age")
            person.save()
            return HttpResponseRedirect("/database")
        else:
            return render(request, "edit.html", {"person": person})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")
     
    # удаление данных из бд
def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/database")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

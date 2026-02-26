from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
import datetime
from .models import Person, Comments

#Main page 
def index(request):

    num_visits=request.session.get('num_visits', 0)

    data = {'num_visits':num_visits}    

    request.session['num_visits'] = num_visits+1

    return render(request, "index.html", context=data)

#Contacts page
def contacts(request):
    return render(request, "contacts.html")

#Comments
def comments(request):
    data = Comments.objects.all()
    return render(request, "comments.html", {"comments": data})

def create_comment(request):
    if request.method == "POST":
        comment = Comments()
        comment.text = request.POST.get("text")
        comment.date = datetime.date.today()
        comment.time = datetime.time()
        comment.save()
    return HttpResponseRedirect("/comments")

#My project
def projects(request):
    return render(request, "projects.html")

#DB interaction
def database(request):
    if request.user.is_authenticated == True:
        people = Person.objects.all()
        return render(request, "database.html", {"people": people})
    else:
        return HttpResponseRedirect("/accounts/login")
    

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

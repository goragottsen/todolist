from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo, User

# Create your views here.
def index(request):
    todos = Todo.objects.all()[:10]
    context = {
        'todos': todos
    }
    return render(request, 'index.html', context)

def details(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        'todo': todo
    }
    return render(request, 'details.html', context)

def add(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']

        todo = Todo(title=title, text=text)
        todo.save()
        return redirect('/todos')
    else:
        return render(request, 'add.html')    

def ajax(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        u = User(
            name = name,
            email = email,
            password = password
        )
        u.save()
    return render(request, 'ajax.html')

# redundand (used before adiing ajax)
def create(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        u = User(
            name = name,
            email = email,
            password = password
        )
        u.save()

        return render(request, 'ajax.html')

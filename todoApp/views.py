from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
# Create your views here.

def getAndPost(request):
    todos = Todo.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        task = Todo.objects.create(title=title, description=description)
        task.save()
    return render(request, 'home.html', {'todos' : todos})
    # return HttpResponse('This is home page')

def updateTodo(request, pk):
    todo = Todo.objects.get(pk=pk)

    if request.method == 'POST':
        todo.title = request.POST.get('newTitle')
        todo.description = request.POST.get('newDescription')
        todo.save()
        return redirect('home')
    return render(request, 'update.html', {'todo': todo})


def deleteTodo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect('home')
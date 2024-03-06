from django.shortcuts import render, redirect
from .models import Todo
from .forms import CreateTodoForm
from django.utils.dateparse import parse_date

def index_page(request):
    if request.method == 'GET':
        form = CreateTodoForm()
        todos = Todo.objects.all()
        return render(request, 'todos/index.html', {'todos': todos, 'form': form})

    if request.method == 'POST':

        form = CreateTodoForm(request.POST)

        if form.is_valid():
            title = form.data.get('title')
            description = form.data.get('description')
            due_date = form.data.get('due_date')
            status = False
            enabled = form.data.get('status')
            if enabled == 'on':
                status = True
            todos = Todo(title=title, description=description, due_date=due_date, status=status)
            todos.save()
        todos = Todo.objects.all()
        return render(request, 'todos/index.html', {'todos': todos, 'form': form})

def todo_details(request, pk):
    todos = Todo.objects.get(id=pk)
    return render(request, 'todos/todo_details.html', {'todos': todos})

def delete_todos(request, pk):
    try:
        todos = Todo.objects.get(id=pk)
        todos.delete()
        return redirect('/todos/')
    except Todo.DoesNotExist:
        return redirect('/todos/')

        #error = "Todos Not Found"
        #form = CreateTodoForm()
        #todos = Todo.objects.all()
        #return render(request, 'todos/index.html', {'todos': todos, 'form': form, 'error': error})


from django.shortcuts import render, redirect
from .models import ToDo

def todo_list(request):
    todos = ToDo.objects.all()
    return render(request, 'todo/todo_list.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        if task:
            ToDo.objects.create(task=task)
        return redirect('todo_list')

def delete_todo(request, todo_id):
    ToDo.objects.filter(id=todo_id).delete()
    return redirect('todo_list')

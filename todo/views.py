from django.shortcuts import render, redirect, get_object_or_404
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

def toggle_complete(request, todo_id):
    todo = get_object_or_404(ToDo, id=todo_id)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todo_list')

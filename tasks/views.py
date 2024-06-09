from django.shortcuts import render, get_object_or_404, redirect
from .models import Task

def index(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})

def new_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        Task.objects.create(title=title, description=description)
        return redirect('index')
    return render(request, 'tasks/task_form.html')

def edit_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.completed = 'completed' in request.POST
        task.save()
        return redirect('index')
    return render(request, 'tasks/task_form.html', {'task': task})

def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('index')

from django.shortcuts import render, redirect
from .models import Task

def task_list(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        Task.objects.create(title=title)
        return redirect('/')

    tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})
from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Task
from .forms import TaskForm

# Главная страница
def index(request):
    status_filter = request.GET.get('status', '')
    if status_filter:
        tasks = Task.objects.filter(status=status_filter).exclude(status='completed')
    else:
        tasks = Task.objects.exclude(status='completed')

    statuses = Task.STATUS_CHOICES
    return render(request, 'tasks/index.html', {'tasks': tasks, 'statuses': statuses})

# Добавление задачи
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm(initial={'due_date': date.today()})  # Устанавливаем текущую дату по умолчанию
    return render(request, 'tasks/add_task.html', {'form': form})

# Редактирование задачи
def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/edit_task.html', {'form': form, 'task': task})
# Удаление задачи
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('index')

# Получение информации о задаче
def task_details(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_details.html', {'task': task})

# AJAX обновление задач
def update_tasks(request):
    status_filter = request.GET.get('status', '')
    if status_filter:
        tasks = Task.objects.filter(status=status_filter).exclude(status='completed')
    else:
        tasks = Task.objects.exclude(status='completed')
    return JsonResponse({'tasks': list(tasks.values())})

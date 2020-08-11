from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator

from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks_list = Task.objects.all().order_by('-created_at')
    paginator = Paginator(tasks_list, 3)
    page = request.GET.get('page')
    tasks = paginator.get_page(page)
    return render(request, 'tasks/list.html', {'tasks': tasks})


def task_view(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task': task})


def new_task(request):
    if (request.method == 'POST'):
        form = TaskForm(request.POST)

        if (form.is_valid()):
            task = form.save(commit=False)
            task.done = 'doing'
            task.save()
            messages.success(request, 'Tarefa adicionada com sucesso')
            return redirect('/')
    else:
        form = TaskForm()
        return render(request, 'tasks/addtask.html', {'form': form})


def edit_task(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)

    if (request.method == 'POST'):
        form = TaskForm(request.POST, instance=task)

        if (form.is_valid()):
            task.save()
            messages.success(request, 'Tarefa editada com sucesso')
            return redirect('/')
        else:
            return render(request, 'tasks/edittask.html', {'form': form, 'task': task})
    else:
        return render(request, 'tasks/edittask.html', {'form': form, 'task': task})


def delete_task(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()

    messages.success(request, 'Tarefa deletada com sucesso')

    return redirect('/')
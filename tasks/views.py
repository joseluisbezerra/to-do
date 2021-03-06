from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.utils.timezone import get_current_timezone
import datetime

from .models import Task
from .forms import TaskForm


@login_required
def task_list(request):

    search = request.GET.get('search')
    filter = request.GET.get('filter')
    tasksDoneRecently = Task.objects.filter(done='done', updated_at__gt=datetime.datetime.now(
        tz=get_current_timezone())-datetime.timedelta(days=30), user=request.user).count()
    tasksDone = Task.objects.filter(done='done', user=request.user).count()
    tasksDoing = Task.objects.filter(done='doing', user=request.user).count()

    if (search):
        tasks = Task.objects.filter(title__icontains=search, user=request.user)
    elif (filter):
        tasks = Task.objects.filter(done=filter, user=request.user)
    else:
        tasks_list = Task.objects.all().order_by(
            '-created_at').filter(user=request.user)
        paginator = Paginator(tasks_list, 3)
        page = request.GET.get('page')
        tasks = paginator.get_page(page)

    return render(request, 'tasks/list.html', {'tasks': tasks, 'tasksrecently': tasksDoneRecently, 'tasksdone': tasksDone, 'tasksdoing': tasksDoing})


@login_required
def task_view(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task': task})


@login_required
def new_task(request):
    if (request.method == 'POST'):
        form = TaskForm(request.POST)

        if (form.is_valid()):
            task = form.save(commit=False)
            task.done = 'doing'
            task.user = request.user
            task.save()
            messages.success(request, 'Tarefa adicionada com sucesso')
            return redirect('/')
    else:
        form = TaskForm()
        return render(request, 'tasks/addtask.html', {'form': form})


@login_required
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


@login_required
def delete_task(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()

    messages.success(request, 'Tarefa deletada com sucesso')

    return redirect('/')


@login_required
def change_status(request, id):
    task = get_object_or_404(Task, pk=id)

    if (task.done == 'doing'):
        task.done = 'done'
    else:
        task.done = 'doing'

    task.save()

    return redirect('/')

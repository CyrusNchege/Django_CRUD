from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import Create_Task_Forms, Update_Task_Forms

# Create your views here.


# read functionality
def task_list(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'tasks/task_list.html', context)

def task_detail(request, id):
    tasks = get_object_or_404(Task, id=id)
    context = {'tasks': tasks}
    return render(request, 'tasks/task_details.html', context)

# create functionality
def create_task(request):
    if request.method == 'POST':
        form = Create_Task_Forms(request.POST)
        if form.is_valid:
            form.save()
            return redirect('tasks:task_list')
    else:
        form = Create_Task_Forms()

    context = {'form':form}

    return render(request, 'tasks/tasks_create.html', context)

# update functionslity
def update_task(request, id):
    task = get_object_or_404(Task, id=id)
    form = Update_Task_Forms(request.POST or None, instance=task)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('tasks:task_list')
    else:
        context = {'form': form}
        return render(request, 'tasks/tasks_update.html', context)

# delete functionality
def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete ()    
    return redirect('tasks:task_list')
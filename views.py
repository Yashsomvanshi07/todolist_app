from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Tasklist
from .forms import TaskForm
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator  # Correct import

def todolist(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "New task added!")
            return redirect('todolist')
    else:
        all_tasks = Tasklist.objects.all()
        form = TaskForm()
        paginator = Paginator(all_tasks, 5)  # Create an instance of the Paginator class
        page = request.GET.get('page')
        all_tasks = paginator.get_page(page)  # Use the paginator instance to paginate tasks
    return render(request, 'base.html', {'all_tasks': all_tasks, 'form': form})


def edit_task(request, task_id):
    task = get_object_or_404(Tasklist, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully!")
            return redirect('todolist')
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form, 'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Tasklist, id=task_id)
    task.delete()
    messages.success(request, "Task deleted successfully!")
    return redirect('todolist')

# View to handle toggling of task completion

def toggle_task(request, task_id):
    task = get_object_or_404(Tasklist, id=task_id)
    task.done = not task.done  # Toggle the completion status
    task.save()
    return JsonResponse({'success': True})  # Return a success response



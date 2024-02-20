from . models import Task
from django.shortcuts import redirect,get_object_or_404,render

# Create your views here.
def addTask(request):
    new_task = request.POST['task']
    Task.objects.create(task = new_task)

    return redirect('home')

def taskDone(request,pk):
    taskdone = get_object_or_404(Task,pk=pk)
    taskdone.is_completed = True
    taskdone.save()
    
    return redirect('home')

def taskUnDone(requst,pk):
    taskundone = get_object_or_404(Task,pk=pk)
    taskundone.is_completed = False
    taskundone.save()

    return redirect('home')

def editTask(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        edited_task = request.POST['edited_task']
        get_task.task = edited_task
        get_task.save()
        return redirect('home')
    else:
        context = {
            'get_task': get_task
        }
        return render(request, 'edit_task.html', context)
    
def deleteTask(request,pk):
    get_task = get_object_or_404(Task,pk=pk)
    get_task.delete()

    return redirect('home')

   
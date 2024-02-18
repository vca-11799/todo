from . models import Task
from django.shortcuts import redirect

# Create your views here.
def addTask(request):
    new_task = request.POST['task']
    Task.objects.create(task = new_task)
    return redirect('home')

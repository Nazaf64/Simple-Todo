from django.shortcuts import render, redirect
from .models import Todo

def home(request):
    todolist = Todo.objects.all()
    context = { 'todolist': todolist }
    return render(request, 'todo/home.html', context)


# Add Task
def addTask(request):
    if (request.method == 'POST'):
        if(request.POST['task'] != ''):
            task = request.POST['task']
            task = Todo(task=task)
            task.save()
            return redirect('/')
        
        elif(request.POST['task'] == ''):
            return redirect('/')
            
# Delete Task
def deleteTask(request, pk):
    if (request.method == 'POST'):
        task = Todo.objects.get(id=pk)
        task.delete()


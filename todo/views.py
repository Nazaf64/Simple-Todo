from django.shortcuts import render, redirect
from .models import Todo
from django.http import HttpResponse

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
            return redirect('home')
        
        elif(request.POST['task'] == ''):
            return redirect('home')
            
# Delete Task
def deleteTask(request, pk):
    if (request.method == 'POST'):
        task = Todo.objects.get(id=pk)
        task.delete()
        
        return HttpResponse('You are not allowed here!!')
        return redirect('home')


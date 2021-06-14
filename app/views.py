from django.shortcuts import redirect, render
from app.models import Todo
from django.core.exceptions import *

# Create your views here.


def home_view(request):
    task_list=Todo.objects.all()
    

    return render(request,'home.html',{'task_list':task_list})


def insert_task(request):
    try:
        task=request.POST.get("task")
        date=request.POST.get("date")
        time=request.POST.get("time")

    
        t=Todo(task=task,date=date,time=time)
   
        t.save()

 
        return redirect("/home")
    except Exception :

        return redirect("/home")    






        

def delete_task(request,id):
    one=Todo.objects.get(id=id)
    one.delete()
    return redirect("/home")
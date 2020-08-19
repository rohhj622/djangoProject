from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# Create your views here.
# Controller 역할


def index(request):
    todos = Todo.objects.all()
    content = {'todos': todos}
    return render(request, 'my_to_do_app/index.html', content)


def createTodo(request):
    user_input_str = request.POST['todoContent']
    new_todo = Todo(content=user_input_str)
    new_todo.save()  # db insert
    return HttpResponseRedirect(reverse('index'))
    #return HttpResponse("createTodo 를 할겅! =>" + user_input_str)
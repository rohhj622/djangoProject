from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# Create your views here.
# Controller 역할


def index(request):
    todos = Todo.objects.all()  # db select * from my_to_do_app_todo
    content = {'todos': todos}
    return render(request, 'my_to_do_app/index.html', content)


def createTodo(request):
    user_input_str = request.POST['todoContent']  # Post 방식으로 실행하므로 request.POST
    new_todo = Todo(content=user_input_str)
    new_todo.save()  # db insert
    return HttpResponseRedirect(reverse('index'))
    # return HttpResponse("createTodo 를 할겅! =>" + user_input_str)


# db엔 남기기
def doneTodo(request):
    user_done_str_id = request.GET['todoNum']  # Get 방식으로 실행하므로 request.GET
    # new_todo = Todo(id=user_done_str_id)
    new_todo = Todo.objects.get(id=user_done_str_id)
    new_todo.isDone = True
    new_todo.save()

    return HttpResponseRedirect(reverse('index'))



# 단순 삭제

# def deleteTodo(request):
#     user_delete_str_id = request.GET['todoNum']  # Get 방식으로 실행하므로 request.GET
#     # new_todo = Todo(id=user_delete_str_id)
#     new_todo = Todo.objects.get(id=user_delete_str_id)
#     new_todo.delete()  # db delete
#
#     return HttpResponseRedirect(reverse('index'))

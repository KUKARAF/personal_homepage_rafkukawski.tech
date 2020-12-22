from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import todo_item
import json
def index(request):
    t = todo_item.objects.get(importance=1)
    return HttpResponse(t.todo_name)

def delete(request, todo_id): 
    todo_item.objects.get(pk=todo_id).delete()
    return HttpResponse('succesfully deleted task %s' % todo_id) 

def template_index(request): 
    todo_list = todo_item.objects.order_by('-due_date')
    template = loader.get_template('todo/index.html')
    context = {
	'todo_list': todo_list
}
    return HttpResponse(template.render(context, request))
def detail(request, todo_id):
    t = todo_item.objects.get(pk=todo_id)
    return HttpResponse(t.todo_name +'<br\>' + t.todo_auth + '<br\>' + str(t.due_date))
def new_item(request):
    todo_name = request.GET.get('todo_name', '')
    #todo_auth = request.GET.get('todo_auth', '')
    due_date = request.GET.get('due_date', '')
    importance = request.GET.get('importance', '1')
    item =  todo_item(todo_name = todo_name, todo_auth = request.user.username, due_date = due_date, importance = importance) 
    item.save()
    
    return HttpResponse(item.todo_id)


def update_item(request, todo_id):    
    t = todo_item.objects.get(pk=todo_id)
    t.todo_name = request.GET.get('todo_name', '')
    t.todo_auth = request.GET.get('todo_auth', '')
    t.due_date = request.GET.get('due_date', '')
    t.importance = request.GET.get('importance', '')
    t.required_time = request.GET.get('required_time', '')
    t.save()
    return HttpResponse('200')


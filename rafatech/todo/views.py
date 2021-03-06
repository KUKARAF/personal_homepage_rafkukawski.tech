from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, JsonResponse
from .models import todo_item
import json
from django.core import serializers
from django.forms.models import model_to_dict


from .forms import ContactForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def user_specific_todo(request,todo_id):

    t = todo_item.objects.filter(todo_auth=request.user.username)
    return t.filter(pk=todo_id)
def index(request):
    t = todo_item.objects.get(importance=1)
    return HttpResponse(t.todo_name)

def delete(request, todo_id): 
    todo_item.objects.get(pk=todo_id).delete()
    return HttpResponse('succesfully deleted task %s' % todo_id) 

def template_index(request): 
    todo_list = todo_item.objects.filter(todo_auth=request.user.username).exclude(status='d').order_by('-due_date')
    template = loader.get_template('todo/index.html')
    context = {
	'todo_list': todo_list
}
    return HttpResponse(template.render(context, request))
def detail(request, todo_id):
    t = todo_item.objects.filter(todo_auth=request.user.username)
    t_spec = t.filter(pk=todo_id)
    data = serializers.serialize('json', t_spec)
    return HttpResponse(data)
   # for item in data:
   #     print(item)
   #     item['product'] = model_to_dict(item['product'])
   # return HttpResponse(json.simplejson.dumps(data), mimetype="application/json")


def new_item(request):
    todo_name = request.GET.get('todo_name', '')
    #todo_auth = request.GET.get('todo_auth', '')
    due_date = request.GET.get('due_date', '')
    print(due_date)
    print("__________________________")
    importance = request.GET.get('importance', '0')
    required_time = request.GET.get('required_time', '1')
    item =  todo_item(todo_name = todo_name, todo_auth = request.user.username, due_date = due_date, importance = importance, required_time = required_time) 
    item.save()
    
    return HttpResponse(item.due_date)


def update_item(request, todo_id):    
    t = todo_item.objects.get(pk=todo_id)
    t.todo_name = request.GET.get('todo_name', '')
    t.todo_auth = request.GET.get('todo_auth', '')
    t.due_date = request.GET.get('due_date', '')
    t.importance = request.GET.get('importance', '')
    t.required_time = request.GET.get('required_time', '')
    t.save()
    return HttpResponse('200')

def status_set(request, todo_id):
    t = todo_item.objects.filter(todo_auth=request.user.username).get(pk=todo_id)
    t.status = request.GET.get('status')
    t.save()
    return HttpResponse(t.status)
        

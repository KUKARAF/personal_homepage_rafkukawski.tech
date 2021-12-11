from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template import loader
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import todo_item
import json
from django.core import serializers
from django.forms.models import model_to_dict
from .forms import ContactForm

def contact_form(request):
    # if this is a POST request we need to process the form data
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid(): 
            print("form is valid!!!!!!")
            # create a form instance and populate it with data from the request:
            # check whether it's valid:
            #if form.is_valid():
            send_mail(
                form.cleaned_data['subject'],
                form.cleaned_data['message']+' \n '+form.cleaned_data['mail'],
                'rafal.kuka94@gmail.com',
                ['rafal.kuka94@gmail.com'],
                )

            #return HttpResponseRedirect('/thanks/')
            #return HttpResponse('200')
            return redirect('/')
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
   #     item['product'] = model_to_dict(item['product'])
   # return HttpResponse(json.simplejson.dumps(data), mimetype="application/json")


def new_item(request):
    todo_name = request.GET.get('todo_name', '')
    #todo_auth = request.GET.get('todo_auth', '')
    due_date = request.GET.get('due_date', '')
    importance = request.GET.get('importance', '0')
    required_time = request.GET.get('required_time', '1')
    item =  todo_item(todo_name = todo_name, todo_auth = request.user.username, due_date = due_date, importance = importance, required_time = required_time) 
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

def status_set(request, todo_id):
    t = todo_item.objects.filter(todo_auth=request.user.username).get(pk=todo_id)
    t.status = request.GET.get('status')
    t.save()
    return HttpResponse(t.status)
        

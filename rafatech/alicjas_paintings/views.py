from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.http import HttpResponseRedirect
from .models import Painting
from .forms import Painting_form


def create_painting(request):
    form = Painting_form(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        print("request method POST")
        if form.is_valid():
            print("form == valid")
            form.save()
            return HttpResponseRedirect('/ap')
        else:
            print("form != valid")
            print(form.errors)
    print(" request method GET rendering normal form")
    return render(request, 'ap/create_painting.html', {'form': form})



def template_index(request):
    paintings = Painting.objects.all()
    print(paintings)
    lang_code = request.LANGUAGE_CODE
    template = loader.get_template('ap/en/home.html')
    context = {
            "Painting": paintings, 
            "lang_code": lang_code 
    }
    return HttpResponse(template.render(context, request))



def template_painting(request, painting_id): 
    painting = Painting.objects.get(pk=painting_id)
    template = loader.get_template('ap/'+lang_code+'_painting.html')
    return HttpResponse(template.render(context, request))

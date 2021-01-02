from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Painting
from .forms import Painting_form

def create_painting(request):
    form = Painting_form(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form':form
            }
    return render(request, "ap/create_painting.html", context)


def template_index(request):
    lang_code = request.LANGUAGE_CODE
    template = loader.get_template('ap/'+lang_code+'_home.html')
    context = {
            "lang_code": lang_code 
    }
    return HttpResponse(template.render(context, request))

















def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def handle_uploaded_file(f):
    with open('test.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


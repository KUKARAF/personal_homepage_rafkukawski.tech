from django.shortcuts import render
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
#from .tokens import account_activation_token
from django.http import HttpResponse
from django.template import loader
import os
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Painting, Imgs
from .forms import Painting_form, Img_form, SignUpForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib import messages
from django.shortcuts import redirect
import time



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/ap')
    else:
        form = SignUpForm()
    return render(request, 'ap/en/signup.html', {'form': form})

def account_activation_sent(request):
    return render(request, 'ap/en/signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'account_activation_invalid.html')

@login_required(login_url="/accounts/login/")
def create_painting(request):
    form = Painting_form(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        print("request method POST")
        if form.is_valid():
            print("form == valid")
            a = form.save().painting_id
            return HttpResponseRedirect('/ap/img/'+str(a))
        else:
            print("form != valid")
            print(form.errors)
    print(" request method GET rendering normal form")
    return render(request, 'ap/create_painting.html', {'form': form})

    


def upload_image(request, painting_id):
    form = Img_form(request.POST or None, request.FILES or None, initial={"painting": Painting.objects.get(pk=painting_id)})
    if request.method == 'POST':
        print("request method POST")
        if form.is_valid():
            print("form == valid")
            form.save()
            #return HttpResponseRedirect('/ap')
            messages.success(request, 'Image Upload successful')
            #form = Img_form()
            success = True
        else:
            print("form != valid")
            print(form.errors)
    print(" request method GET rendering normal form")
    return render(request, 'ap/img_form.html', {'form': form})

def template_index(request):
    paintings = Painting.objects.all()
    imgs = {}
    for p in paintings:
        path = p.upload
    lang_code = request.LANGUAGE_CODE
    template = loader.get_template('ap/en/home.html')
    context = {
            "Painting": paintings, 
            "lang_code": lang_code, 
    }
    return HttpResponse(template.render(context, request))


def template_painting(request, painting_id): 
    painting = Painting.objects.get(pk=painting_id)
    images = Imgs.objects.filter(painting=painting_id)
    lang_code = request.LANGUAGE_CODE
    
    print(lang_code)
    template = loader.get_template('ap/'+lang_code+'/painting.html')
    return HttpResponse(template.render({"painting":painting, "images":images}, request))

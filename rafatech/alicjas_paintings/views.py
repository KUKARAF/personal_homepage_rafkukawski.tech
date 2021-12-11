from django.shortcuts import render
from django.http import FileResponse
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
#from .tokens import account_activation_token
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import Painting, Imgs, Cart_items
from .forms import Painting_form, Img_form, SignUpForm, LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import  login,logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib import messages
from django.shortcuts import redirect
from django.core import serializers
import time


def purchase_form(request):
    # if this is a POST request we need to process the form data
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid(): 
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
def logout_view(request):
    logout(request)
    return render(request, 'ap/en/logout.html') 
def login(request):
    form = LoginForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            if user is not None:
                login(request, user) 
                return redirect('/ap')
            else:
                return redirect('/ap/login')
        else: 
            return render(request, 'ap/en/login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'ap/en/login.html', {'form': form})

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

@login_required(login_url="/ap/login/")
def create_painting(request):
    form = Painting_form(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            a = form.save().painting_id
            return HttpResponseRedirect('/ap/img/'+str(a))
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
      
@login_required(login_url="/ap/login/")
def cart_index_json(request):
    ciu = Cart_items.objects.all().filter(owner_id=request.user.id) 
    paintings = ciu.values_list('painting_id', flat=True)
    imgs = []
    for p in paintings:
        imgs.append(Painting.objects.get(painting_id=p) )  
    painting_list = serializers.serialize('json', imgs)
    return HttpResponse(painting_list, content_type="text/json-comment-filtered")

 
#@login_required(login_url="/ap/login/")
def cart_index(request, painting_id = "all"):
    lang_code = request.LANGUAGE_CODE
    if(painting_id == "all" ):
        template = loader.get_template('ap/en/checkout.html')
    else:
        template = loader.get_template('ap/en/checkout_single.html')
    context = { "cont" : painting_id  }
    return HttpResponse(template.render(context, request))
    #return render(request, template, context)

 
@login_required(login_url="/ap/login/")
def cart_add(request, painting_id):
    logged_in_user = User.objects.get(pk=request.user.id)
    painting_to_add = Painting.objects.get(pk=painting_id )
    Cart_items.objects.create( owner_id=logged_in_user, painting_id = painting_to_add ) 
    html = "<html><body>added painting nr"+str(painting_id)+" to "+str(logged_in_user)+"'s cart</body></html>" 
    return HttpResponse(html)

@login_required(login_url="/ap/login/")
def cart_rm(request, painting_id):
    logged_in_user = User.objects.get(pk=request.user.id)
    i = Cart_items.objects.filter(owner_id=request.user.id).filter(painting_id=painting_id ) 
    i.delete()
    html = "<html><body>ok</body></html>" 
    return HttpResponse(html)

@login_required(login_url="/ap/login/")
def painting_rm(request, painting_id):
    logged_in_user = User.objects.get(pk=request.user.id)
    i = Painting.objects.filter(painting_id=painting_id ) 
    i.delete()
    html = "<html><body>ok</body></html>" 
    return HttpResponse(html)

def template_painting(request, painting_id): 
    painting = Painting.objects.get(pk=painting_id)
    images = Imgs.objects.filter(painting=painting_id)
    lang_code = request.LANGUAGE_CODE
    
    template =loader.select_template(['ap/'+lang_code+'/painting.html','ap/en/painting.html'])
    #template = loader.get_template('ap/'+lang_code+'/painting.html')
    context = {"painting":painting, "images":images}
    return HttpResponse(template.render(context, request))


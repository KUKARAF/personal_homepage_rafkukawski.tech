from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.shortcuts import render, redirect

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
                ['edebowskamoczydlowska@gmail.com'],
                )

            #return HttpResponseRedirect('/thanks/')
            #return HttpResponse('200')
            return redirect('/aglu')
    return render(request, 'contact.html', {'form': form})

# Create your views here.

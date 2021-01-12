from django import forms

class ContactForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    mail = forms.CharField(label='email', max_length=100)
    message = forms.CharField(label='message', max_length=500)


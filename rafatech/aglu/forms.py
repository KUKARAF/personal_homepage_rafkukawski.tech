from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(label='subject', max_length=100)
    mail = forms.CharField(label='sender', max_length=100)
    message = forms.CharField(label='message', max_length=500)


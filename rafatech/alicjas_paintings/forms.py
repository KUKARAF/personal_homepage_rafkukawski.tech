from django import forms
from .models import Painting, Imgs
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from django.middleware.csrf import get_token
class Painting_form(forms.ModelForm):
    class Meta:
        model = Painting 
        fields = [
                "painting_name",
                "painting_author",
                "painting_date",
                "painting_price",
                "painting_desc",
                "painting_dimensions", 
                "upload"
                ]


class Img_form(forms.ModelForm):
    class Meta:
        model = Imgs 
        fields = [
                "painting",
                "image"
                ]



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    def __init__(self, *args, **kwargs):
        helper = FormHelper()
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()


    class Meta:
        model = User
        fields = ( 'first_name', 'last_name', 'username','email', 'password1', 'password2', )

from django import forms
from .models import Painting

class Painting_form(forms.ModelForm):
    class Meta:
        model = Painting 
        fields = [
                "painting_name",
                "painting_author",
                "painting_date",
                "painting_price",
                "painting_desc",
                "upload"
                ]


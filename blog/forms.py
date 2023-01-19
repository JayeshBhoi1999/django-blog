from django import forms

from .models import Comment
from django.forms import Textarea

class CommentFrom(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','email','body']
        widgets = {
            'body': Textarea(attrs={
                'class': "form-control",
                'style': 'max-width: 260px;',
                'placeholder': 'body'
                })
        }


# blog/forms.py

from django import forms
from blog import models

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = [
            'post',
            'name',
            'email',
            'text',
        ]
        labels = {
            'text': 'Comment'
        }
        widgets = {
            'post': forms.HiddenInput()
        }


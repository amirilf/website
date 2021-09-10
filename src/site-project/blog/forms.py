# form model
# from ckeditor import fields
from django import forms

# models
from .models import Comment

class CommentForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id':'title-message',
                'name':'title-message',
                'class':'form-control form-control-sm sm bg-light',
                'type':"text", 
                'placeholder': "Write your name",
            }
        )
    )

    desc = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'name':"text-message", 
                'id':"text-message",
                'cols':30,
                'rows':5,
                'class':"form-control form-control-sm bg-light",
                'placeholder': "Write your comment",
            }
        )
    )

    class Meta:
        model = Comment
        fields = [
            'name',
            'desc'
        ]
# form model
# from ckeditor import fields
from django import forms

# models
from .models import Comment

class CommentForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            # input attributes of the person's name
            attrs={
                'id'          :'title-message',
                'name'        :'title-message',
                'class'       :'form-control form-control-sm sm bg-light',
                'type'        :"text", 
                'placeholder' : "Write your name",
            }
        )
    )

    desc = forms.CharField(
        widget=forms.Textarea(
            # input attributes of the person's comment
            attrs={
                'name'       :"text-message", 
                'id'         :"text-message",
                'cols'       :30,
                'rows'       :4,
                'class'      :"form-control form-control-sm bg-light",
                'placeholder': "Write your comment",
            }
        )
    )

    # determine fields in model
    class Meta:
        model  = Comment
        fields = [
            'name',
            'desc'
        ]
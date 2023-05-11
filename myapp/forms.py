from django import forms
from .models import PostModel,Comment

class PostModelform(forms.ModelForm):
    content=forms.CharField(widget=forms.Textarea(attrs={'rows':2,'cols': 29}))
    class Meta:
        model=PostModel
        fields=('title','content','image')

class PostUpdate_Form(forms.ModelForm):
    class Meta:
        model=PostModel
        fields=('title','content','image')
        

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('content',)
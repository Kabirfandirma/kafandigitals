from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your name', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your email', 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your comment', 'class': 'form-control', 'rows': 4}),
        }

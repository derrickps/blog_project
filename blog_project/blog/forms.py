from django import forms
from blog.models import Comment

class EmailSendForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'sendername','style': 'background:black;'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'sendername','style': 'background:black;'}))
    to = forms.EmailField(widget=forms.TextInput(attrs={'class':'sendername','style': 'background:black;'}))
    comments = forms.CharField(required=False,widget=forms.Textarea(attrs={'style':'background:black;'}))

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','email','body')
        widgets = {
            'email': forms.EmailInput(attrs={
            'class': 'form-control',
            'style': 'background-color: black',
            'placeholder': 'Your Email',
            }),
            'name': forms.TextInput(attrs={
            'class': 'form-control',
            'style': 'background-color: black',
            'placeholder': 'Your Name'
            }),
            'body': forms.Textarea(attrs={
            'style': 'background-color: black',
            'class': 'form-control',
            'placeholder': 'Comment Here,'})
         }

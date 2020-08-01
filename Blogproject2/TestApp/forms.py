from django import forms
from TestApp.models import Comment, Feedback
class EmailSendForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    to=forms.EmailField(label="SendTo")
    comments=forms.CharField(required="False",widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=("name","email","body")

from django.contrib.auth.models import User
class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']


class FeedbackForm(forms.ModelForm):
    class Meta:
        model=Feedback
        fields="__all__"

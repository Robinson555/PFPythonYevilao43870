from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Message

class MessageForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}))
    receiver = forms.ModelChoiceField(label="To", queryset=User.objects.all())

from django import forms
from home import models

class HomeForm(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'write a post',
        }
    ))

    class Meta:
        model = models.Post
        fields =  ('post',)
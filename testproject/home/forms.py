from django import forms
from home import models

class HomeForm(forms.ModelForm):
    post = forms.CharField()

    class Meta:
        model = models.Post
        fields =  ('post',)
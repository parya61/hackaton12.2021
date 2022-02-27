from .models import Articles
from django.forms import ModelForm,TextInput,Textarea
from django import forms


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['start', 'finish']

        widgets = {
            "start":Textarea(attrs = {
            'placeholder': 'Введите текст'
            }),
            "finish":TextInput(attrs = {
            'placeholder': ''
            })
        }
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

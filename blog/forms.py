from django import forms
from .models import Contact, Your_email, Forma





class PostForms(forms.ModelForm):
    class Meta:
        model = Forma
        fields = '__all__'



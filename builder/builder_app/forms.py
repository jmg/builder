from django import forms
from models import Project

class ProjectForm(forms.ModelForm):
        
    user = forms.CharField(widget=forms.HiddenInput)
    long_description = forms.CharField(widget=forms.Textarea)    
        
    class Meta:
        
        model = Project
        exclude = ("user",)

    
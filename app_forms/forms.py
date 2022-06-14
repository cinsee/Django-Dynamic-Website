from django import forms

class AppForm(forms.Form):
    question = forms.CharField(max_length=255, required=True, label="label")
    placehold = forms.CharField(max_length=255, required=True, label="placeholder")
    
class Option(forms.Form):
    value = forms.CharField(max_length=100,required=True,label="option")

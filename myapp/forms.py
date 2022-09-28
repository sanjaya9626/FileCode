from django import forms

class people_details(forms.Form):
    name=forms.CharField(max_length=100)
    email=forms.CharField(max_length=40)
    address=forms.CharField(max_length=50)
    age=forms.IntegerField()
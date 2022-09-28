from django.shortcuts import render
from . import forms
# Create your views here.

def people_view(request):
    form=forms.people_details()
    my_dict={'form':form}
    return render(request, 'hello/input.html',context=my_dict)
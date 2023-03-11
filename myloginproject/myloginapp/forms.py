

from django import forms

from myloginapp.models import MyUser


class MyuserForm(forms.ModelForm):
    # username = forms.CharField(max_length=255)
    # email = forms.CharField(max_length=255)
    # phone = forms.CharField(max_length=15)
    # fullname = forms.CharField(max_length=255)
    # password = forms.CharField(max_length=255)

    class Meta:
        model = MyUser
        # fields = "__all__"
        exclude = ["user_id", ]

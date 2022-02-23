from django import forms


class Registration(forms.Form):
    First_name = forms.CharField()
    Last_name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()

class Login(forms.Form):
    email = forms.CharField()
    password = forms.CharField()
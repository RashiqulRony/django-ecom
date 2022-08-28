from django import forms


class UserValidation(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    confirm_password = forms.CharField(required=True)

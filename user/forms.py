from django import forms


class UserForm(forms.Form):
    siape = forms.IntegerField()
    email = forms.EmailField()

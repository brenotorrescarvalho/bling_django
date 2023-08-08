from django import forms

class GetAuthorizationForm(forms.Form):
    client_id = forms.CharField(widget = forms.TextInput(attrs = {'placeholder': 'please type here your client id;'}))

class GetTokenForm(forms.Form):
    authorization_code = forms.CharField(widget = forms.TextInput(attrs = {'placeholder': 'please type here your authorization code;'}))
    client_secret = forms.CharField(widget = forms.TextInput(attrs = {'placeholder': 'please type here your client secret;'}))
    
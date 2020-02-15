from django import forms
from .models import ChurchInformation, SongRequest



class RegistrationForm(forms.ModelForm):
    regno = forms.CharField(required=True, widget=forms.TextInput(attrs={"maxlength":150}))
    church_name = forms.CharField(required=True,widget=forms.TextInput(attrs={"maxlength":150}))
    firstname = forms.CharField(required=False,widget=forms.TextInput(attrs={"maxlength":150}))
    lastname = forms.CharField(required=False,widget=forms.TextInput(attrs={"maxlength":150}))
    address = forms.CharField(required=True,widget=forms.TextInput(attrs={"maxlength":150}))
    phone = forms.CharField(required=True,widget=forms.TextInput(attrs={"maxlength":150}))
    alternative_phone = forms.CharField(required=True,widget=forms.TextInput(attrs={"maxlength":150}))
    web = forms.CharField(required=False,widget=forms.TextInput(attrs={"maxlength":150}))
    email = forms.CharField(required=True,widget=forms.EmailInput(attrs={"maxlength":150}))

    class Meta:
        model = ChurchInformation
        exclude = ['license_type']

class SongRequestForm(forms.ModelForm):
    date_for = forms.CharField(required=True, widget=forms.DateInput(attrs={"type":"date"}))
    class Meta:
        model = SongRequest
        exclude = ['church','created']


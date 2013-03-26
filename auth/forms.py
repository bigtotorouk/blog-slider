from django import forms
from blogme.models import UserProfile
class UserForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)
    password2 = forms.CharField(max_length=50)
    email = forms.EmailField()
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from accounts.models import Profile

class UserForm(forms.ModelForm):
    username = forms.IntegerField(widget= forms.TextInput
                           (attrs={'placeholder':'Enter RUID'}))
    email = forms.EmailField(widget= forms.TextInput
                           (attrs={'placeholder':'Enter email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))
    class Meta:
        model = User
        fields = ("username", "email", "password")
    def save (self):
        password = self.cleaned_data.pop('password')
        u = super().save()
        u.set_password(password)
        u.save()
        return u

class ProfileForm(forms.ModelForm):
    picture = forms.ImageField(required = False)
    name =  forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'Enter Name'}))
    email_id = forms.EmailField(widget= forms.TextInput
                           (attrs={'placeholder':'Enter another email'}))
    phone_number = forms.IntegerField(widget= forms.TextInput
                           (attrs={'placeholder':'Enter Mobile Number'}))
    birth_date = forms.DateField(widget= forms.TextInput
                           (attrs={'placeholder':'Date of Birth'}))
    service_number = forms.IntegerField(widget= forms.TextInput
                           (attrs={'placeholder':'Enter Service Number'}))
    designation = forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'Enter Designation'}))
    railway_zone = forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'Railway Zone'}))

    class Meta:
        model = Profile
        fields = ('name', 'email_id', 'phone_number','birth_date','service_number','designation','railway_zone','sex','picture')

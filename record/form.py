from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import OurRecord


class UserCreationSelfForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control w-50'}), label="Password",
                                required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control w-50'}), label="Re-Password",
                                required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

        widgets = {'username': forms.TextInput(attrs={'class': 'form-control w-50'}),
                   'first_name': forms.TextInput(attrs={'class': 'form-control w-50'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control w-50'}),
                   'email': forms.TextInput(attrs={'class': 'form-control w-50'}),

                   }


class RecordForm(forms.ModelForm):
    class Meta:
        model = OurRecord
        fields = ['time', 'shop', 'item', 'price']

        widgets = {'shop': forms.TextInput(attrs={'class': 'form-control w-50'}),
                   'item': forms.TextInput(attrs={'class': 'form-control w-50'}),
                   'time': forms.DateTimeInput(attrs={'class': 'form-control w-50'}),
                   'price': forms.NumberInput(attrs={'class': 'form-control w-50'}),
                   }

        labels = {'shop': 'Location/shop', 'item': 'Description/item'}


class AmountSetUpForm(forms.Form):
    # total_amount = forms.NumberInput(attrs={'class':'form-control w-50'})
    # total_consumed = forms.NumberInput(attrs={'class':'form-control w-50'})

    total_amount = forms.FloatField(initial=0.0, required=True, max_value=10000000000)
    total_consumed = forms.FloatField(initial=0.0, required=True, max_value=10000000000)


class AddForm(forms.Form):
    add_amount = forms.FloatField(initial=0.0, max_value=1000000000)


class SubForm(forms.Form):
    sub_amount = forms.FloatField(initial=0.0, max_value=1000000000)

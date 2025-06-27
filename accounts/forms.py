from django import forms
from .models import Account

class Registrationform(forms.ModelForm):
    password = forms.CharField(widget= forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'class' : 'form-control',
    }))
    confirm_password = forms.CharField(widget= forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
    }))
    class Meta:
        model = Account
        fields =  ['first_name', 'last_name', 'phone_no', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super(Registrationform, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email-id'
        self.fields['phone_no'].widget.attrs['placeholder'] = 'Phone Number'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super(Registrationform, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "Why your password is not matching ?"
            )        
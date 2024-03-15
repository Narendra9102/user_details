from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'age', 'date_of_birth']

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            validate_email(email)
        except ValidationError:
            raise forms.ValidationError("Invalid email address")
        return email

    def clean_age(self):
        age = self.cleaned_data['age']
        if not isinstance(age, int):
            raise forms.ValidationError("Age must be a valid integer")
        return age

from django import forms
from first_project.models import User


class NewUser(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

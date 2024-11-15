from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Task

class TaskForm(forms.ModelForm):
    due_date = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(
            attrs={
                'placeholder': 'DD/MM/YYYY',
                'type': 'text',  
            }
        )
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date']

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Add Task'))
        
        
        
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Optionally, you can customize the error messages for the whole form
        error_messages = {
            'username': {
                'max_length': 'Your username must be 150 characters or fewer.',
                'invalid': 'Use letters, digits, and @/./+/-/_ only.',
            },
            'password1': {
                'password_too_similar': 'Your password can’t be too similar to your other personal information.',
                'password_too_common': 'Your password can’t be a commonly used password.',
                'password_entirely_numeric': 'Your password can’t be entirely numeric.',
            },
        }

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
      
        self.fields['username'].error_messages.update({
            'max_length': 'Please keep your username under 150 characters.',
            'invalid': 'Please use valid characters in your username.',
        })






class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField(label="Enter your email", max_length=254)
    
    
    
    

# forms.py
from django import forms

class SetNewPasswordForm(forms.Form):
    new_password1 = forms.CharField(label="New password", widget=forms.PasswordInput)
    new_password2 = forms.CharField(label="Confirm new password", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("new_password1")
        password2 = cleaned_data.get("new_password2")
        if password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data
    
    
from django import forms
from django.contrib.auth.forms import SetPasswordForm

class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(CustomSetPasswordForm, self).__init__(*args, **kwargs)
        self.fields['new_password1'].help_text = None  # Remove help text
        self.fields['new_password2'].help_text = None  # Remove help text
    
    

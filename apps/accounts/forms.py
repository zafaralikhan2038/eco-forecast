from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm as DjangoPasswordChangeForm
from .models import CustomUser

class CustomUserChangeForm(UserChangeForm):
    """
    A form for updating users.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Add custom classes to form fields
        custom_class = "block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-green-500 transition duration-300 ease-in-out"
        
        for field_name, field in self.fields.items():
            if hasattr(field.widget, 'attrs'):
                field.widget.attrs.update({'class': custom_class})
    
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'profile_photo',
            'is_active'
        )

class CustomUserCreationForm(UserCreationForm):
    """
    A form for creating new users.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Add custom classes to form fields
        custom_class = "block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-green-500 transition duration-300 ease-in-out"
        
        for field_name, field in self.fields.items():
            if hasattr(field.widget, 'attrs'):
                field.widget.attrs.update({'class': custom_class})
    
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'profile_photo',
            'password1',
            'password2'
        )

class LoginForm(forms.Form):
    """
    Form for user login
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ProfilePhotoForm(forms.ModelForm):
    """
    Form for updating profile photo
    """
    class Meta:
        model = CustomUser
        fields = ['profile_photo']

class CustomPasswordChangeForm(DjangoPasswordChangeForm):
    """
    Custom password change form with Tailwind CSS styling
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Add custom classes to form fields
        custom_class = "block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-green-500 transition duration-300 ease-in-out"
        
        for field_name, field in self.fields.items():
            if hasattr(field.widget, 'attrs'):
                field.widget.attrs.update({
                    'class': custom_class,
                    'placeholder': field.label
                })
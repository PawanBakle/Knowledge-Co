from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Role

class CustomerForm(UserCreationForm):
    # Explicitly define role field with choices
    role = forms.ModelChoiceField(
        queryset=Role.objects.all(),
        empty_label="Select Role",
        widget=forms.Select  # Ensures dropdown rendering
    )

    # Explicitly define experience level field
    experience_level = forms.ChoiceField(
        choices=CustomUser.EXP,
        widget=forms.Select  # Ensures dropdown rendering
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'role', 'experience_level']
        
    def clean(self):
        cleaned_data = super().clean()
        
        # Additional validation if needed
        role = cleaned_data.get('role')
        experience_level = cleaned_data.get('experience_level')
        
        if not role:
            self.add_error('role', 'Role is required')
        
        return cleaned_data
from django import forms
from .models import Profile, Plant


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['profile_picture']
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Enter a username..'
            }),
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Enter a first name..'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Enter a last name..'
            })
        }


class CreatePlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'
        exclude = ['profile']
        widgets = {
            'plant_type': forms.Select(attrs={
                'placeholder': 'Choose a plant type:'
            }),
            'name': forms.TextInput(attrs={
                'placeholder': 'Plant Name'
            }),
            'image_url': forms.URLInput(attrs={
                'placeholder': 'Choose an image'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Enter a Description'
            }),
            'price': forms.NumberInput(attrs={
                'placeholder': 'Enter Price'
            })
        }


class DeletePlantForm(CreatePlantForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

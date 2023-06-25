from django import forms
from .models import Profile, Fruit


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['image_url', 'age']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Last Name'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email'
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Password', 'autocomplete': 'off', 'toggle-password': 'password'
            }),
        }


class CreateFruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Fruit Name'
            }),
            'image_url': forms.URLInput(attrs={
                'placeholder': 'Fruit Image URL'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Fruit Description'
            }),
            'nutrition': forms.Textarea(attrs={
                'placeholder': 'Nutrition Info'
            }),
        }


class DeleteFruitForm(CreateFruitForm):
    class Meta(CreateFruitForm.Meta):
        exclude = ['nutrition']

    def __init__(self, *args, **kwargs):
        super(DeleteFruitForm, self).__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['email', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

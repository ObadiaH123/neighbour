from django import forms
from .models import Post,Profile
from django.contrib.auth.models import User


class UploadForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image','caption')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('photo','name','bio')

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email')

class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'photo', 'bio']

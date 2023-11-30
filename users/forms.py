from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Profile
        fields = ['user', 'email', 'password1', 'password2', 'profile_pic', 'bio ']


class UserUpdateForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    email = forms.EmailField()

    class Meta:
        model = Profile  # Use the Profile model instead of the default User model
        fields = ['user', 'email', 'image']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['title', 'content']
#         widgets = {
#             'content': CKEditorWidget(attrs={'rows': 50, 'cols': 100}),
#         }
#
#
# class PostUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['title', 'content']
#         widgets = {
#             'content': CKEditorWidget(attrs={'rows': 1000, 'cols': 1000}),
#         }

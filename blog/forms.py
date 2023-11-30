from django import forms
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.forms import UserCreationForm
from .models import Article
from django.contrib.auth.models import User


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['headline', 'sub_headline', 'image', 'body', 'featured', 'tags', 'status']
        widgets = {
            'body': CKEditorWidget(attrs={'rows': 50, 'cols': 100}),
        }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

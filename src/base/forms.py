from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView

from base.models import Post
from django.contrib.auth.forms import UserCreationForm


class LoginForm(LoginView):
    # username = forms.CharField(max_length=63, label='Username')
    # password = forms.CharField(max_length=63, widget=forms.PasswordInput)
    template_name = 'base/lbhogin.html'


class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        template_name = 'base/register.html'
        fields = ['username', 'first_name', 'last_name', 'adress', 'birthdate']
        help_texts = {
            'username': None,
            'first_name': None,
            'last_name': None,
            'email': None,
            'password': None,
            'adress': None,
            'birthdate': None,
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'title', 'image']


class ProfilPictureForm(forms.Form):
    profil_pic = forms.ImageField()


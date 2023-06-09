from django import forms
from .models import Furniture
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class FurnitureForm(forms.ModelForm):
    class Meta:
        model = Furniture
        fields = ['name', 'description', 'price', 'exist']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'floatingInput',
                    'placeholder': 'Название'
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Описание'
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Цена'
                }
            ),
            'exist': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                    'placeholder': 'В наличии?'
                }
            ),
            'photo': forms.FileInput(
                attrs={
                    'placeholder': 'Фото'
                }
            ),
        }


class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        label='Логин пользователя',
        widget=forms.TextInput(attrs={'class': 'form-control', })
    )
    email = forms.CharField(
        label='Электронная почта',
        widget=forms.EmailInput(attrs={'class': 'form-control', })
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control', })
    )
    password2 = forms.CharField(
        label='Повторите пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control', })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Введите ваш логин',
        widget=forms.TextInput(attrs={'class': 'form-control', })
    )
    password = forms.CharField(
        label='Введите ваш пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control', })
    )


class ContactForm(forms.Form):
    subject = forms.CharField(
        label='Заголовок письма',
        widget=forms.TextInput(
            attrs={'class': 'form-control', },
        )
    )
    content = forms.CharField(
        label='Тело письма',
        widget=forms.Textarea(
            attrs={'class': 'form-control',
                   'rows': 11, },
        )
    )

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from authapp.models import User

import hashlib
import random

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['password'].widget.attrs['placeholder'] = 'Введите пароль'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'


class UserRegisterform(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserRegisterform, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['palaceholder'] = 'Введите имя пользователя'
        self.fields['email'].widget.attrs['palaceholder'] = 'Введите адрес эл. почты'
        self.fields['first_name'].widget.attrs['palaceholder'] = 'Введите имя'
        self.fields['last_name'].widget.attrs['palaceholder'] = 'Введите фамилию'
        self.fields['password1'].widget.attrs['palaceholder'] = 'Введите пароль'
        self.fields['password2'].widget.attrs['palaceholder'] = 'Подтвердите пароль'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'

    def save(self, commit=True):
        user = super().save()
        user.is_active = False
        salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()
        user.activation_key = hashlib.sha1(str(user.email + salt).encode('utf8')).hexdigest()
        user.save()
        return user


class UserProfileForm(UserChangeForm):
    avatar = forms.ImageField(widget=forms.FileInput(), required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'avatar', 'username', 'email', 'age')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['username'].widget.attrs['readonly'] = True
        self.fields['email'].widget.attrs['readonly'] = True
        self.fields['avatar'].widget.attrs['class'] = 'custom-file-input'
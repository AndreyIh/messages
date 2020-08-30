from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User


class UserLoginForm(forms.Form):
    username = forms.CharField(label='Ник',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            qs = User.objects.filter(username=username)
            if not qs.exists():
                raise forms.ValidationError('Пользователь с таким ником не зарегистрирован')
            if not check_password(password, qs[0].password):
                raise forms.ValidationError('Неверный пароль')
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Этот пользователь неактивен')
        return super(UserLoginForm, self).clean()


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(
                               attrs={'class': 'form-control my-1 py-1',
                                      'type': "username"}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
                               attrs={'class': 'form-control my-1 py-1',
                                      'type': "password"}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(
                                attrs={'class': 'form-control my-1 py-1',
                                       'type': "password"}))

    class Meta:
        model = User
        fields = ('username', 'password',)

    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError('Пароли не совпадают!!!')
        if data['password'] == data['username']:
            raise forms.ValidationError('Пароль совпадает с логином!!!')
        return data['password2']

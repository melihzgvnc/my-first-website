from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import MyUser

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=100, label='E-Posta Adresi', widget=forms.EmailInput)
    password = forms.CharField(max_length=100, label='Şifre', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = [     
            'email',
            'password',            
        ]

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError('E-Posta adını veya parolayı yanlış girdiniz!')
            return super(LoginForm, self).clean()

"""
class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=100, label='Kullanıcı Adı')
    email = forms.EmailField(max_length=100,label='E-Posta',widget=forms.EmailInput)
    password1 = forms.CharField(max_length=100, label='Parola', widget=forms.PasswordInput)            
    password2 = forms.CharField(max_length=100, label='Parola Doğrulama', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Parolalar eşleşmiyor")
        return password2

"""
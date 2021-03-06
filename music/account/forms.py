from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import Textarea

from account.models import UserProfile


class UserForm(forms.ModelForm):
    username = forms.CharField(label='帳號')
    password = forms.CharField(widget=forms.PasswordInput(), label='密碼')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='確認密碼')
    
    class Meta:
        model = User
        fields = ('username', 'password')
        
    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password!=password2:
            raise forms.ValidationError('密碼不相符')
        return password2


class UserProfileForm(forms.ModelForm):
    fullName = forms.CharField(max_length=128, label='姓名')

    class Meta:
        model = UserProfile
        fields = ('fullName', )
        
        
class PhotoUrlForm(forms.ModelForm):
    photoUrl = forms.CharField(max_length=128, label='個人大頭貼')
      
    class Meta:
        model = UserProfile
        fields = ('photoUrl', )
        
        
class ProfileForm(forms.ModelForm):
    profile = forms.CharField(label='個人簡介', widget=Textarea(attrs={'rows':7, 'cols':50}))
    
    class Meta:
        model = UserProfile
        fields = ('profile', )
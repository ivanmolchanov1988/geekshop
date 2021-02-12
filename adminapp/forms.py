from authapp.forms import UserRegisterform, UserProfileForm
from authapp.models import User
from django import forms

class UserAdminRegisterform(UserRegisterform):
    avatar = forms.ImageField(widget=forms.FileInput(), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'avatar')

        def __init__(self, *args, **kwargs):
            super(UserAdminRegisterform, self).__init__(*args, **kwargs)
            self.fields['avatar'].widget.attrs['class'] = 'custom-file-input'



class UserAdminProfileForm(UserProfileForm):

    def __init__(self, *args, **kwargs):
        super(UserAdminProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = False
        self.fields['email'].widget.attrs['readonly'] = False
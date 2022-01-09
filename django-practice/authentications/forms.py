from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from authentications.models import Profile

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['firstname','lastname','phone','profile_pic']
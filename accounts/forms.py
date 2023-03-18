from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser  # from the current dir import it


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("name","phone_number") #this name from the customized models
        


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields

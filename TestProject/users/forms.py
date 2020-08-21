from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User


# to Create User
class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email': 'Email'}


# for Update User Profile
class UpdateProfile(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


# for Update Admin Profile
class UpdateAdminProfile(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = '__all__'


# For Update user permissions
class UpdateUserPermissions(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['user_permissions', 'is_active']

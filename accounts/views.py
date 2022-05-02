from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.views import PasswordChangeView, LoginView
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from .forms import SignUpForm, EditProfileForm, ChangePasswordForm
from blogapp.models import User, Profile
from django.urls import  reverse_lazy, reverse
from django.http import HttpResponseRedirect

class UserRegisterView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEditView(UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user

class ChangePasswordView(PasswordChangeView):
    template_name = 'registration/change-password.html'
    form_class = ChangePasswordForm
    success_url = reverse_lazy('home')

class ProfileView(DetailView):
    model = User
    template_name = 'profile.html'


def CreateProfile(request):
    #print(request.user)

    if (hasattr(request.user, 'profile')):
        print("profile already exists")
    else:
        profile=Profile()
        profile.user=request.user
        profile.bio="No bio yet"
        profile.save()

    return HttpResponseRedirect(reverse('home'))

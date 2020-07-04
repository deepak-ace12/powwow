from django import forms
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, reverse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from .models import Profile
from .forms import SignUpForm, UpdateProfileForm, UpdateUserForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def update_profile(request):
    if request.method == 'POST':
        user = Profile.objects.get(user=request.user)
        form = UpdateProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
    else:
        user = Profile.objects.get(user=request.user)
        form = UpdateProfileForm(instance=user)
    return render(request, 'update_profile.html', {'form': form})


@login_required
def update_user(request):
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('update_profile'))
    else:
        form = UpdateUserForm(instance=request.user)
    return render(request, 'update_user.html', {'form': form})



from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
# from django.views.generic import ListView, DetailView, CreateView, TemplateView
# from django.urls import reverse_lazy
# from django.contrib.auth.mixins import LoginRequiredMixi
from jobservice import settings
from .forms import CustomUserCreationForm, UserLoginForm, CustomUserChangeForm
from .models import CustomUser


class EditProfile(UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name_suffix = '_update_form'

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, pk=self.request.user.pk)

    success_url = reverse_lazy('home')
    # slug_field = 'email'


def user_logout(request):
    logout(request)
    return redirect('user_login')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})


def user_registration(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'You are successfully registered!')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            return redirect('home')
        else:

            messages.error(request, 'Registration Error')

    else:
        form = CustomUserCreationForm()

    return render(request, 'users/register.html', {'form': form})

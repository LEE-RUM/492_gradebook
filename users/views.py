from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from users.models import Role
from .forms import UserRegisterForm, UserUpdateForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin

# register view
class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})

    def  post(self, request):
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid(): #check if form is valid, if so save form
            user = form.save(commit=False)
            role, created = Role.objects.get_or_create(id=Role.STUDENT) #creates role
            user.role = role
            user.save() #user saved
            messages.success(request, f'Your account has been created! You are now able to log in') #message pops up once succesfuly registered
            return redirect('users:login') #redirects user once registered
        return render(request, 'users/register.html', {'form': form})

#same as the regular registration, differes with the fact that its a different role
class TeacherRegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})

    def  post(self, request):
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            role, created = Role.objects.get_or_create(id=Role.TEACHER)
            user.role = role
            user.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('users:login')
        return render(request, 'users/register.html', {'form': form})

# profile view, must be logged in to view this
class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        form = UserUpdateForm(instance=request.user)

        context = {
            'form': form,
        }

        return render(request, 'users/profile.html', context) #renders the profile page

    def post(self, request):
        form = UserUpdateForm(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('users:ProfileView')
        context = {
            'form': form,
        }
        return render(request, 'users/profile.html', context) #renders the profile page



# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.forms import UserForm,ProfileForm
from . import models
from django.views.generic import TemplateView,ListView,DetailView
from django.db import  transaction
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from mysite import urls
from . import models
import time


def LogInView(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                # return render(request,'classroom/questions.html')
                # return redirect(classroom.views.question)
                return HttpResponseRedirect('/')
            else:
                content_dic={'error':'You are a Inactive User Contact Admin'}
                return render(request,'accounts/login.html',context=content_dic)
        else:
            content_dic={'error':'Invalid Roll Number or Password'}
            return render(request,'accounts/login.html',context=content_dic)
    else:
        return render(request,'accounts/login.html')

# def logout_user(request):
#     logout(request)
#     messages.success(request,('You have been Logged out.'))
#     return redirect('fav')

@transaction.atomic
def signup(request):

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.refresh_from_db()
            profile_form.full_clean()
            profile_form = ProfileForm(request.POST, instance=user.profile)
            profile_form.save()
            return redirect('login')


    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    return render(request, 'accounts/signup.html', {
        'user_form': user_form,
        'profile_form': profile_form

    })


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return HttpResponseRedirect('/accounts/login/')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'accounts/signup.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


def profile (request):
    return render(request,'accounts/profile.html' , {'user' : request.user})

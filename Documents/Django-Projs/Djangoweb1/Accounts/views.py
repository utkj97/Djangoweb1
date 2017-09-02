# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate , login
from django.contrib.auth.models import User
from .forms import UserForm
from django import forms
from django.views.generic import View

class UserFormView(View):
    form_class = UserForm
    template_name = 'registration/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit = False)
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password']

            user.set_password(password)
            email = form.cleaned_data['email']

            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user.first_name = first_name
                user.last_name = last_name
                user = authenticate(first_name=first_name,last_name=last_name,username=username, password=password,email=email)
                if user is not None:
                    if user.is_active:
                        login(request,user)
                        return redirect('Music:index')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')

        else:
            form = self.UserForm()
        return render(request,self.template_name,{'form':'form'})









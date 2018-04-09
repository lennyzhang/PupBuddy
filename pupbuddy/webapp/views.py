from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from webapp.models import *
from webapp.forms import *

# Create your views here.

@login_required
def main(request):
    context = {}
    return render(request, "main.html", context)
    
def register(request):
    context = {}
    if request.method == "GET":
        context["form"] = RegistrationForm()
        return render(request, "Register.html", context)
    form = RegistrationForm(request.POST, request.FILES)
    context["form"] = form
    if not form.is_valid():
        return render(request, "Register.html", context)
    new_user = User.objects.create_user(username = form.cleaned_data["username"], password = form.cleaned_data["password1"])
    new_user.save()
    user = Profile.objects.create(
        username = form.cleaned_data["username"], 
        deviceNumber = form.cleaned_data["deviceNumber"]
    )
    user.save()
    new_user = authenticate(username = form.cleaned_data["username"], password = form.cleaned_data["password1"])
    login(request, new_user)
    return redirect('main')
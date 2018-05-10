from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from webapp.models import *
from webapp.forms import *
import sys
sys.path.append('/home/pi/Desktop/webapp/Pupbuddy/pupbuddy/webapp')
from motorControl import *
from django.shortcuts import HttpResponse

# Create your views here.

@login_required
def main(request):
    context = {}
    return render(request, "main.html", context)
    
def register(request):
    context = {}
    if request.method == "GET":
        context["form"] = RegistrationForm()
        return render(request, "register.html", context)
    form = RegistrationForm(request.POST, request.FILES)
    context["form"] = form
    if not form.is_valid():
        return render(request, "register.html", context)
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


def receive_command(request, command):
    robot = PupBuddy()
    context = {}
    if (command == "S"):
        print("Stop")
        robot.dcStop();
    elif (command == "F"):
        print("Forward")
        robot.dcForward()
    elif (command == "B"):
        print("Backward")
        robot.dcBackward()
    elif (command == "L"):
        print("Left")
        robot.dcTurnLeft()
    elif (command == "R"):
        print("Right")
        robot.dcTurnRight()
    elif (command == "A"):
        print("Launch")
        robot.launchTreat()
    elif (command == "LF" or command == "FL"):
        print("Forward & Left")
        robot.dcForLeft()
    elif (command == "RF" or command == "FR"):
        print("Forward & Right")
        robot.dcForRight()
    elif (command == "LB" or command == "BL"):
        print("Backward & Left")
        robot.dcBackLeft()
    elif (command == "RB" or command == "BR"):
        print("Backward & Right")
        robot.dcBackRight()
    elif (command == "LA" or command == "AL"):
        print("Left & Launch")
        robot.dcTurnLeft()
    elif (command == "RA" or command == "AR"):
        print("Right & Launch")
        robot.dcTurnRight()
    elif (command == "FA" or command == "AF"):
        print("Forward & Launch")
    elif (command == "BA" or command == "AB"):
        print("Backward & Launch")
        robot.dcForward()
    return HttpResponse('')


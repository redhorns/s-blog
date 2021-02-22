from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from .models import UserProfile
from django.contrib import messages





def myregister(request) :

    if request.method == "POST" :

        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')


        if password1 != password2 :
            msg = "Passwords dont match"
            messages.success(request, msg)

            return redirect('home')

        if len(password1) < 8 :
            msg = "Password needs to be at least 8 character long"
            messages.success(request, msg)

            return redirect('home')

        

        # success
        if len(User.objects.filter(email=email)) == 0:

            user = User.objects.create_user(username=email, email=email, first_name=username, password=password1, is_staff=True, is_superuser=False, is_active=True)
            # group = Group.objects.get(name='users')
            # user.groups.add(group)

            profile = UserProfile(
                user = user,
                name = username,
                email = email,
            )
            profile.save()

            msg = "Voilà, Now you are only one step away. Go ahead and sign in !"
            messages.success(request, msg)

            return redirect('home')
            
        else : 
            msg = "You are already registered, try signing in !"
            messages.success(request, msg)
            
            return redirect('home')


    return redirect('home')


def mylogin(request) :

    if request.method == 'POST' :

        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        user = authenticate(username=email, password=password)

        if user != None :

            try :
                user_profile = UserProfile.objects.get(user=user)
            except :
                user_profile = None
            
            login(request, user)

            if user_profile != None:
                msg = "Welcom back, " + str(user_profile.name)
            messages.success(request, msg)

            request.session['username'] = user.first_name
            request.session['email'] = user.email

            return redirect('home')

        else : 

            failure = "failure"

            return render(request, 'back/authenticate/login.html', {
                'failure': failure,
            })


    return redirect('home')


def mylogout(request):

    logout(request)

    return redirect('home')



def admin_login(request) :

    if request.method == 'POST' :

        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        user = authenticate(username=email, password=password)

        if user != None :

            try :
                user_profile = UserProfile.objects.get(user=user)
            except :
                user_profile = None
            
            login(request, user)

            request.session['username'] = user.first_name
            request.session['email'] = user.email

            return redirect('home')

        else : 

            failure = "failure"

            return render(request, 'back/authenticate/login.html', {
                'failure': failure,
            })


    return render(request, 'back/authenticate/login.html')


def admin_logout(request):

    logout(request)

    return redirect('home')


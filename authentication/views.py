from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login as auth_login,logout
from .models import *

def login(request):

    context={
        "error":""
    }

    if request.method == "POST":

        user = authenticate(username = request.POST['username'] ,password = request.POST['password'] )

        if user is not None:

            auth_login(request, user)

            return redirect('/book/home/')
        
        else:

            context={
                "error":"*Invalid username or password"
            }

            return render(request,"authentication/loginpage.html",context)    

    return render(request,'authentication/loginpage.html',context)

def logoutpage(request):

    logout(request)

    return redirect('/')

def signuppage(request):

    context = {
        "error":""
    }

    if request.method == "POST":

        user_check = User.objects.filter(username = request.POST['username'])

        if len(user_check) >0 :

            context = {
                "error":"*Username already exist"
            }

        else:

            new_user = User(username = request.POST['username'],first_name = request.POST['firstname'],
                            last_name = request.POST['lastname'],email = request.POST['email_address'],
                            age = request.POST['age'])
            
            new_user.set_password(request.POST['password'])

            new_user.save()

            return redirect('/')

    return render(request,'authentication/signuppage.html',context)
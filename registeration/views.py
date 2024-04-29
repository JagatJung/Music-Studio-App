from django.shortcuts import render,  redirect
from django.http import HttpResponse, JsonResponse
from django.db import connection
from registeration.dbActions import checkUser
from users.dbActions import insertUser

def login(request):
    if request.method == "POST":
        uid = checkUser(request.POST['user'], request.POST['password'])
        if uid == -1:
            return render(request, "login_form.html")
        else:
            request.session['username'] = uid
            return redirect("/user")
        
    return render(request, "login_form.html")

def register(request):
    if request.method == "POST":
        button_value =request.POST['submit'].split('_')
    
        if (button_value[0] == 'insert'):
            insertUser(request.POST['first_name_register'], request.POST['last_name_register'], request.POST['email_register'], request.POST['phone_register'],request.POST['dob_register'], request.POST['gender_register'], request.POST['address_register'])
            return render(request, "login_form.html")
        
    return render(request, "registration.html")

def delSession(request):
    del request.session['username']
    return render(request, "login_form.html")




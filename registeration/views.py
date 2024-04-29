from django.shortcuts import render,  redirect
from django.http import HttpResponse, JsonResponse
from django.db import connection
from registeration.dbActions import checkUser, resetPwdDB
from users.dbActions import insertUser
import registeration.validateActions  as VDA

def login(request):
    if request.method == "POST":
        if VDA.validate_email(request.POST['user']) and VDA.validate_password(request.POST['password']):
            uid = checkUser(request.POST['user'], request.POST['password'])
            if uid[0] == -1:
                return render(request, "login_form.html", {'msg':'invalid username or password'})
            else:
                request.session['username'] = uid[0]
                request.session['name'] = uid[1]
                return redirect("/user")
        else:
            return render(request, "login_form.html", {'msg': 'invalid username or password' })
    if 'msg' in request.session:
        return render(request, "login_form.html", {'msg': request.session['msg'] })
    return render(request, "login_form.html")

def register(request):
    if request.method == "POST":
        button_value =request.POST['submit'].split('_')
    
        if (button_value[0] == 'insert'):
            msg = insertUser(request.POST['first_name_register'], request.POST['last_name_register'], request.POST['email_register'], request.POST['phone_register'],request.POST['dob_register'], request.POST['gender_register'], request.POST['address_register'])
            request.session['msg'] = msg
            return redirect('/')
        
    return render(request, "registration.html")

def resetpwd(request):
    if request.method == "POST":
        button_value =request.POST['submit'].split('_')

        if (button_value[0] == 'insert'):
            msg = resetPwdDB(request.POST['user'], request.POST['code'], request.POST['password'])
            request.session['msg'] = msg
            return redirect('')
        
    return render(request, "pwdreset.html")

def delSession(request):
    del request.session['username']
    return redirect("/")




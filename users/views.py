from django.shortcuts import render, redirect
from django.http import HttpResponse
from users.dbActions import getUsers, dlt_user, updateUser, insertUser, resetPasswordUser
from registeration.sessionCheck import session_required
from registeration.views import delSession

@session_required
def user(request):
    if request.method == "POST":
        button_value =request.POST['submit'].split('_')

        if(button_value[0] == 'dlt') :
            if(int(button_value[1]) == request.session['username']):
                msg = "You can not delete your own account"
                return render(request, "user_dash.html",  {'users': getUsers, 'username': request.session['name'], 'msg': msg})
            else:
                msg = dlt_user(button_value[1])
                return render(request, "user_dash.html",  {'users': getUsers, 'username': request.session['name'], 'msg': msg})
            
        elif (button_value[0] == 'update') :
            msg = updateUser(request.POST['first_name'], request.POST['last_name'], request.POST['email'], request.POST['phone'],request.POST['dob'], request.POST['gender'], request.POST['address'], button_value[1])
            return render(request, "user_dash.html",  {'users': getUsers, 'username': request.session['name'], 'msg': msg})

        elif (button_value[0] == 'insert'):
            msg = insertUser(request.POST['first_name_register'], request.POST['last_name_register'], request.POST['email_register'], request.POST['phone_register'],request.POST['dob_register'], request.POST['gender_register'], request.POST['address_register'])
            return render(request, "user_dash.html",  {'users': getUsers, 'username': request.session['name'], 'msg': msg})
        
        elif (button_value[0] == 'resetPassword'):
            msg = resetPasswordUser(button_value[1])
            if(int(button_value[1]) == request.session['username']):
                request.session['msg'] =  msg
                del request.session['username']
                return redirect('/')
            # add code that id its users own account than his session is destroyed
            return render(request, "user_dash.html",  {'users': getUsers, 'username': request.session['name'], 'msg': msg})

        
        return render(request, "user_dash.html",  {'users': getUsers, 'username': request.session['name']})

    return render(request, "user_dash.html",  {'users': getUsers, 'username': request.session['name']})


    # Optionally, you can return the results to a template or as JSO

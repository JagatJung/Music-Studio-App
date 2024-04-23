from django.shortcuts import render
from django.http import HttpResponse
from users.dbActions import getUsers, dlt_user, updateUser, insertUser, resetPasswordUser


def user(request):
    if request.method == "POST":
        if request.method == "POST":
            button_value =request.POST['submit'].split('_')

            if(button_value[0] == 'dlt') :
                dlt_user(button_value[1])
                return render(request, "user_dash.html",  {'users': getUsers})
            
            elif (button_value[0] == 'update') :
                updateUser(request.POST['first_name'], request.POST['last_name'], request.POST['email'], request.POST['phone'],request.POST['dob'], request.POST['gender'], request.POST['address'], button_value[1])
                return render(request, "user_dash.html",  {'users': getUsers})

            elif (button_value[0] == 'insert'):
                insertUser(request.POST['first_name_register'], request.POST['last_name_register'], request.POST['email_register'], request.POST['phone_register'],request.POST['dob_register'], request.POST['gender_register'], request.POST['address_register'])
                return render(request, "user_dash.html",  {'users': getUsers})
            
            elif (button_value[0] == 'resetPassword'):
                resetPasswordUser(button_value[1])
                # add code that id its users own account than his session is destroyed
                return render(request, "user_dash.html",  {'users': getUsers})

            
            return render(request, "user_dash.html",  {'users': getUsers})
        return render(request, "user_dash.html",  {'users': getUsers})
    return render(request, "user_dash.html",  {'users': getUsers})


    # Optionally, you can return the results to a template or as JSO

from django.shortcuts import render
from django.http import HttpResponse
from users.dbActions import getUsers, dlt_user, updateUser


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
            
            return render(request, "user_dash.html",  {'users': getUsers})
        return render(request, "user_dash.html",  {'users': getUsers})
    return render(request, "user_dash.html",  {'users': getUsers})


    # Optionally, you can return the results to a template or as JSO

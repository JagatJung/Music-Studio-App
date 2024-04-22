from django.shortcuts import render
from django.http import HttpResponse
from users.dbActions import getUsers


def user(request):
    return render(request, "user_dash.html",  {'users': getUsers})


    # Optionally, you can return the results to a template or as JSO

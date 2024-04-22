from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection


def login(request):
    if request.method == "POST":
        return render(request, "registration.html")
    return render(request, "login_form.html")

    # Optionally, you can return the results to a template or as JSO

from functools import wraps
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect

def session_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.session.get('username'):
            return redirect("")
        return view_func(request, *args, **kwargs)
    return _wrapped_view


    
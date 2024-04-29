from functools import wraps
from django.http import HttpResponseForbidden

def session_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.session.get('username'):
            return HttpResponseForbidden("Session required to access this page.")
        return view_func(request, *args, **kwargs)
    return _wrapped_view
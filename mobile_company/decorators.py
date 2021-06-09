from django.shortcuts import redirect
from django.http import HttpResponse


def unathenticated_user(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('customer')
        else:
            return func(request, *args, **kwargs)

    return wrapper


def allowed_users(allowed_users=[]):
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_users:
                return func(request, *args, **kwargs)
            else:
                return HttpResponse('Error')

        return wrapper
    return decorator




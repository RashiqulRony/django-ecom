from django.shortcuts import redirect


def is_login(function):
    def wrapper(request, *args, **kw):
        if request.user.is_authenticated:
            return function(request, *args, **kw)
        else:
            return redirect('/users/logout')

    return wrapper

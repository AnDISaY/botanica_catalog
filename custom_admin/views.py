from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth import login, logout, authenticate

from .forms import LoginForm


def logout_required(
    function=None, redirect_field_name="next", login_url=None
):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: not u.is_authenticated,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


@logout_required(login_url='/custom_admin')
def sign_in(request):
    form = LoginForm()
    if request.method == 'POST':
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            login(request, user)
            return redirect('/custom_admin')
    return render(request, 'admin/signin.html', {"form": form,})


@login_required(login_url='/custom_admin/login')
def custom_admin(request):
    form = LoginForm()
    if request.method == 'POST' and request.POST['logout'] == 'True':
        logout(request)
        return render(request, 'admin/signin.html', {"form": form,})
    return render(request, 'admin/home.html', {"user": request. user})

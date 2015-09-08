from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.forms.forms import NON_FIELD_ERRORS
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from people.models import Lifter
from .form import LoginForm, RegistrationForm

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        form.full_clean()
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        try:
            user = User.objects.create_user(username, email, password)
            user.save()

        except Exception as e:
            raise(e)
        else:
            Lifter(user=user).save()
            user.first_name = fname
            user.last_name = lname
            user.save()
        return HttpResponseRedirect(reverse("main"))
    else:
        form = RegistrationForm()

    return render(
        request,
        "register.html",
        {"form": form}
    )

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        form.full_clean()
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect(reverse("main"))
        else:
            # Return an 'invalid login' error message.
            form.errors[NON_FIELD_ERRORS] = form.error_class(
                ['Please enter a valid username and password.']
            )
    else:
        form = LoginForm()

    return render(request, "login.html", {'form': form})
        

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

import hashlib
from django.core.signing import Signer, BadSignature
from django.core.urlresolvers import reverse_lazy
from django.db import IntegrityError
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from django.views.generic.edit import FormView
from people.models import Lifter
from guildboard.forms import DivErrorList
from .form import EmailForm, RegistrationForm, LoginForm


class EmailRegistration(FormView):
    template_name = "email.html"
    form_class = EmailForm
    success_url = reverse_lazy("email_registration")

    def get_context_data(self, **kwargs):
        context = super(EmailRegistration, self).get_context_data(**kwargs)
        context['page_title'] = "Sign Up"
        context['form_title'] = "Email"
        return context

    def form_valid(self, form):
        return super(EmailRegistration, self).form_valid(form)


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        form.full_clean()
        if form.is_valid():
            password = request.POST['password']
            email = request.POST['email'].lower().strip()
            fname = request.POST['first_name'].strip()
            lname = request.POST['last_name'].strip()
            try:
                user = User.objects.create_user(email, email, password)
                user.save()

            except IntegrityError:
                messages.error(
                    request,
                    "There is already an account associated "
                    "with that email address."
                )

            except Exception as e:
                raise(e)
            else:
                user.first_name = fname
                user.last_name = lname
                # user.is_active = False
                # signer = Signer()
                # hasher = hashlib.md5()
                # hasher.update(bytes(
                #     "%s%s%s" % (user.pk, user.last_name, user.first_name),
                #     encoding="utf-8"
                # ))
                # token = signer.sign(hasher.hexdigest())
                user.save()
                lifter = Lifter(user=user)
                lifter.save()
                # send_activation_email(request, lifter)
                messages.success(
                    request,
                    "Your account has been created! Please log in."
                )
                return HttpResponseRedirect(reverse("home"))
    else:
        form = RegistrationForm()

    return render(
        request,
        "register.html",
        {"form": form}
    )


def resend_activation_view(request, lifter):
    lifter_obj = Lifter.objects.get(pk=lifter)

    send_activation_email(request, lifter_obj)

    return render(
        request,
        "login.html",
        {"form": LoginForm()}
    )


def send_activation_email(request, lifter):
    base_url = "http://" + request.get_host()
    activation_url = base_url + reverse("activate_acct", args=[lifter.auth_token])

    send_mail(
        subject="Activate your Barbell Open account",
        from_email="admin@barbellopen.com",
        recipient_list=[lifter.user.email],
        message="Please click the link below to activate your account.",
        html_message=r'<p>Thanks for making an account for the Barbell Open! Click the link to activate your account. Once it is active, you may register for the Open.</p><p><a href="%s">Activate!</a></p>' % activation_url
    )

    messages.success(
        request,
        "An email has been sent to activate your account."
        " Please activate it now to log in. Be sure to check your spam folder!"
    )


def activate_acct(request, auth_token):
    signer = Signer()
    try:
        signer.unsign(auth_token)
    except BadSignature:
        raise Exception("well, shit")

    try:
        lifter = Lifter.objects.get(auth_token=auth_token)
    except Lifter.DoesNotExist:
        raise Exception("well, shit")
    else:
        lifter.user.is_active = True
        lifter.user.save()
        messages.success(
            request,
            "Your account has been activated! Please log in and sign up for a competition."
        )
    return HttpResponseRedirect(reverse("login"))


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST, error_class=DivErrorList)
        form.full_clean()
        email = request.POST['email'].lower().strip()
        password = request.POST['password']

        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
                return HttpResponseRedirect(reverse("home"))
            else:
                resend_url = reverse("resend_activation", args=[user.lifter.pk])
                messages.error(
                    request,
                    "This account has not been activated yet. "
                    "<a href='%s'>Resend activation email.</a> "
                    "Be sure to check your spam folder!" % resend_url
                )
        else:
            print("*"*80)
            print(user)
            print(request.POST['email'])
            print(request.POST['password'])
            messages.error(
                request,
                "Please enter a valid username and password."
            )

    else:
        form = LoginForm(error_class=DivErrorList)

    return render(request, "login.html", {'form': form})


def logout_view(request):
    logout(request)
    print("*"*80)
    return HttpResponseRedirect(reverse("records"))

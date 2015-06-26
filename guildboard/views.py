from django.shortcuts import render

from django.views.generic import  View
from django.contrib.auth.decorators import login_required


class LoginRequiredView(View):

    @classmethod
    def as_view(cls, **kwargs):
        return login_required(
            super(LoginRequiredView, cls).as_view(**kwargs),
            login_url='/login/'
        )

def main(request):
    return render(
        request,
        "base.html"
    )

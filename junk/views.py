from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.template import loader
from .models import Group


def change_theme(request, **kwargs):
    if 'is_dark_theme' in request.session:
        request.session["is_dark_theme"] = not request.session.get('is_dark_theme')
    else:
        request.session["is_dark_theme"] = False
    return HttpResponseRedirect(request.META.get("HTTP_REFERRER", "/"))


class GroupListView(ListView):
    model = Group
    template_name = "myfirst.html"

from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from .models import Group
from .forms import DayForm, DayFormSet, PlayerForm


def change_theme(request, **kwargs):
    if 'is_dark_theme' in request.session:
        request.session["is_dark_theme"] = not request.session.get('is_dark_theme')
    else:
        request.session["is_dark_theme"] = False
    return HttpResponseRedirect(request.META.get("HTTP_REFERRER", "/"))


class GroupListView(ListView):
    model = Group
    template_name = "myfirst.html"

    def get_context_data(self, **kwargs):
        context = super(GroupListView, self).get_context_data(**kwargs)
        context['form'] = PlayerForm()
        return context


def home(request):
    # form = DayFormSet(request.POST or None)
    form = DayForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()

    return render(request, 'myfirst.html', context={'form': form})


def create_day(request):
    # form = DayForm(request.POST or None)
    form = DayForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("home")

    return render(request, 'day.html', context={'form': form})


def create_player(request):
    form = PlayerForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()

    return render(request, 'player.html', context={'form': form})

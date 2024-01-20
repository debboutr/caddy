from django.http import HttpResponse
from django.template import loader


def index(request):
    """here is where you would put lines to grab data from the DB"""
    template = loader.get_template("myfirst.html")
    return HttpResponse(template.render())

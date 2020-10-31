from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome to Mme's Creations Online Store!")

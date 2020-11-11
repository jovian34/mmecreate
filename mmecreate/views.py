from django.shortcuts import redirect
import os


def home(request):
    if os.environ.get('CONSTRUCTION'):
        return redirect('mmestore/construction', request)
    return redirect('/mmestore', request)

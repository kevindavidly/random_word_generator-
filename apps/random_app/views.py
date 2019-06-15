from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string 

def index(request):
    context = {
    "random":get_random_string(length=14) 
    }
    if not "counter" in request.session :
        request.session['counter'] = 1
    else:
         request.session['counter'] += 1

    return render(request,"random_app/index.html", context)

def clear(request):
    request.session.clear()
    return redirect('/')

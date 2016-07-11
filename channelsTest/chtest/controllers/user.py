from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from preserialize.serialize import serialize
from django.shortcuts import render, redirect

def user(request):
    if 'user_details' in request.session.keys():
        return render(request,'user.html')
    stri=get_random_string(length=32)
    session_details = {'random':stri}
    print "client session start"
    print stri
    request.session['user_details'] = session_details
    return render(request,'user.html')

from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import *
from django.core.mail import send_mail

from datetime import datetime
import datetime as dt
import requests

#from .forms import UserForm




def RaySendMail(request, subject, message, to_email):

	send_mail(
	    subject,
	    message,
	    'info@oilreach.co.uk',
	    [to_email,],
	    fail_silently=False,
	)



def IndexView(request):
	if request.method == "POST":
		pass


	else:
		context = {}
		return render(request, "main/index.html", context )

def ProjectsView(request):
	if request.method == "POST":
		pass


	else:
		context = {}
		return render(request, "main/projects.html", context )


def AboutView(request):
	if request.method == "POST":
		pass


	else:
		context = {}
		return render(request, "main/about.html", context )

def ServiceView(request):
	if request.method == "POST":
		pass


	else:
		context = {}
		return render(request, "main/service.html", context )


def ContactView(request):
    form = ContactForm(request.POST)
    context = {'form':form,}
    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            message = form.cleaned_data.get('message')
            try:
                data = Contact()
                data.name = name
                data.email = email
                data.phone = phone
                data.message = message
                data.save()
                messages.success(request, "Message has been delivered")
                return redirect(reverse('contact'))
            except:
                
                messages.warning(request, form.errors)
        else:
            messages.warning(request, form.errors)

    return render(request, 'main/contact.html', context)
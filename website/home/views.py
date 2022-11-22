from django.contrib.humanize.templatetags.humanize import naturaltime, intcomma
import requests
import uuid
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from django.views import View
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMessage
from django.forms import modelformset_factory
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils import timezone
from django.urls import reverse_lazy
from django.db.models import Count
import hmac
import hashlib
import json
from django.views.decorators.csrf import csrf_exempt
# from testimonial.models import *
# from about.models import *
# from projects.models import *
# from training.models import Training
from .models import *
from mass.models import *
from priests.models import *
from gallery.models import *




import datetime
import calendar




import logging

logger = logging.getLogger(__name__)



def home(request):
	priests = Priest.objects.all()
	try:
		gallery = Gallery.objects.all()
	except:
		gallery = None

	# for i in gallery:
	# 	check = i.title.occasion.all()[0]
	# 	print("check")
	# 	print(type(check))
	try:
		video = AdvertVideo.objects.all()[0]
	except:
		video = None

	today = str(datetime.datetime.now().strftime('%x'))

	today = str(datetime.datetime.now().strftime('%x'))
	try:
		slider = Slider.objects.all()
	except:
		slider = None
	try:
		event = Event.objects.filter(event_type="Celebration").order_by('event_start_date')
		for i in event:
			event_date = str(i.event_start_date.strftime('%x'))
			if event_date >= today:
				event = i
				break
	except:
		event= None

	try:
	    event1 = []
	    event2 = Event.objects.filter(event_type="Celebration").order_by('event_start_date')
	    for i in event2:
	        event_date = str(i.event_start_date.strftime('%x'))
	        if event_date >= today:
	            event1.append(i)

	except:
		event1= None
	try:
		#mass_obj = Event.objects.filter(event_type="Mass").order_by('event_start_date')
		mass_obj = Event.objects.order_by('event_start_date')
		mass = []
		for i in mass_obj:
			mass_date = str(i.event_start_date.strftime('%x'))
			if mass_date >= today:
				mass.append(i)
	except:
		mass = None
	context = {
    	'event': event,
    	'event1': event1,
    	'mass': mass,
    	'priests': priests,
    	'slider':slider,
    	'video': video,
    	'gallery': gallery
	}
	return render(request, 'home/home.html', context)
	#return render(request, 'home/home-index.html', context)




def events(request):
	today = str(datetime.datetime.now().strftime('%x'))
	try:
		mass_obj = Event.objects.filter(event_type="Celebration").order_by('event_start_date')
		mass = []
		for i in mass_obj:
			mass_date = str(i.event_start_date.strftime('%x'))
			if mass_date >= today:
				mass.append(i)
	except:
		mass = None
	context = {
    	'mass': mass,
	}
	return render(request, 'home/event-list.html', context)


def event_detail(request, id, slug):
	today = str(datetime.datetime.now().strftime('%x'))
	try:
		event = get_object_or_404(Event, id=id, slug=slug)
	except:
		event = None
	try:
		mass_obj = Event.objects.filter(event_type="Celebration").order_by('event_start_date')
		mass = []
		for i in mass_obj:
			mass_date = str(i.event_start_date.strftime('%x'))
			if mass_date >= today:
				mass.append(i)
	except:
		mass = None
	context = {
    	'event': event,
    	'mass': mass,
	}
	return render(request, 'home/event-details.html', context)


def slider(request):
	today = str(datetime.datetime.now().strftime('%x'))
	try:
		slider = Slider.objects.all()
	except:
		slider = None
	context = {
    	'slider': slider,
	}
	return render(request, 'home/event-list.html', context)
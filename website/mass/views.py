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




import datetime
import calendar




import logging

logger = logging.getLogger(__name__)







# def home(request):
# 	if request.method == 'POST':
# 		event = None
# 	else:
# 		today = datetime.datetime.now()
# 		month_decimal = int(today.strftime('%m'))
# 		year_decimal = int(today.strftime('%Y'))
# 		no_days_month = int(calendar.monthrange(year_decimal, month_decimal)[1])
# 		last_day_date_month = datetime.datetime(year_decimal, month_decimal, no_days_month)
# 		event = Event.objects.filter(
# 			event_date__range=[today,last_day_date_month]).order_by(
# 			'event_date')
# 	context = {
#     	'event': event,
# 	}
# 	return render(request, 'home/home.html', context)

#




# month_obj = Month.objects.get(month=month)
# year_decimal = int(request.POST['year'])
# year_obj = Year.object.get(year=year_decimal)
# no_days_month = int(calendar.monthrange(year_decimal, month_decimal)[1])
# first_day_date_month = datetime.datetime(year_decimal, month_decimal, 1)
# last_day_date_month = datetime.datetime(year_decimal, month_decimal, no_days_month)
# fast_track = FastTrack.objects.filter(month=month_obj, year=year_obj).filter(
# date_of_flight__range=[first_day_date_month,last_day_date_month]).order_by(
# 			'date_of_flight')



# def home(request):
# 	today = str(datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
# 	try:
# 		event = Event.objects.filter(event_type="Celebration").order_by('-event_date')
# 		for i in event:
# 			event_date = str(i.event_date.strftime('%d-%m-%Y %H:%M:%S'))
# 			if event_date >= today:
# 				event = i
# 				break
# 	except:
# 		event= None

# 	try:
# 		mass_obj = Event.objects.filter(event_type="Mass").order_by('-event_date')
# 		print(mass_obj)
# 		mass = []
# 		for i in mass_obj:
# 			mass_date = str(i.event_date.strftime('%d-%m-%Y %H:%M:%S'))
# 			if today >= mass_date:
# 				mass.append(i)
# 	except:
# 		mass = None
# 	context = {
#     	'event': event,
#     	'mass': mass,
# 	}
# 	return render(request, 'home/home.html', context)



def mass(request):
	today = str(datetime.datetime.now().strftime('%x'))
	try:
		mass = Mass.objects.all()
	except:
		mass = None
	context = {
    	'mass': mass,
	}
	return render(request, 'mass/mass-list.html', context)



def mass_details(request, id, slug):
	mass = get_object_or_404(Mass, id=id, slug=slug)
	context = {
		'mass': mass,
	}
	return render(request, 'mass/mass.html', context)


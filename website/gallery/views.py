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
from home.models import *




import datetime
import calendar




import logging

logger = logging.getLogger(__name__)




def gallery(request):
	try:
		event = Event.objects.filter(event_type="Celebration").order_by('event_start_date')
	except:
		event= None
	context = {
    	'event': event
	}
	return render(request, 'gallery/gallery.html', context)
	# return render(request, 'gallery/pictures.html', context)
	# return render(request, 'gallery/gal.html', context)




def gallery_detail(request, id, slug):
	try:
		event = get_object_or_404(Event, id=id, slug=slug)
	except:
		event = None
	context = {
    	'event': event
	}
	return render(request, 'gallery/gallery_details.html', context)
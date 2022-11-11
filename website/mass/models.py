from __future__ import unicode_literals

from django.db import models
from authentication.models import User
import uuid
from django.urls import reverse
from django.db.models.fields import BLANK_CHOICE_DASH
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.core.mail import send_mail
from django.conf import settings
# Create your models here.
from home.models import *



class Mass(models.Model):
    objects = models.Manager()      #Our default Manager
    published = PublishedManager()  #Our Custom Model Manager

    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published'),
    )

    STATUS_EVENT_TYPE = (
        ('mass','Mass'),
        ('celebration','Celebration'),
    )

    status              =       models.CharField(max_length=10, choices=BLANK_CHOICE_DASH + list(STATUS_CHOICES))
    event_type          =       models.CharField(max_length=10,blank=True, null=True, choices=BLANK_CHOICE_DASH + list(STATUS_CHOICES))
    category            =       models.DateTimeField(blank=True, null=True)
    title               =       models.CharField(max_length=400)
    slug                =       models.SlugField(max_length=200, blank=True, null=True)
    event_start_date    =       models.DateTimeField(blank=True, null=True)
    event_end_date      =       models.DateTimeField(blank=True, null=True)
    image_1024_by_300   =       models.ImageField(blank=True, null=True)
    snippet             =       models.TextField(blank=True, null=True)
    body                =       models.TextField(blank=True, null=True)
    cost                =       models.DateTimeField(blank=True, null=True)
    venue               =       models.TextField(blank=True, null=True)
    organizer           =       models.CharField(max_length=400, blank=True, null=True)
    phone_number        =       models.CharField(max_length=400, blank=True, null=True)
    website             =       models.CharField(max_length=400, blank=True, null=True)
    email_organizer     =       models.EmailField(max_length=100, blank=True, null=True)
    quote               =       models.TextField(blank=True, null=True)
    quote_author        =       models.CharField(max_length=400, blank=True, null=True)
    view_count          =       models.PositiveIntegerField(default=0)
    created             =       models.DateTimeField(auto_now_add=True)
    updated             =       models.DateTimeField(auto_now=True)



    class Meta:
        ordering = ['-event_start_date']
        verbose_name = 'Mass'
        verbose_name_plural = 'Mass'

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("mass:mass_detail", args=[self.id, self.slug])



@receiver(pre_save, sender=Mass)
def pre_save_slug1(sender, **kwargs):
    slug = slugify(kwargs['instance'].title)
    kwargs['instance'].slug = slug






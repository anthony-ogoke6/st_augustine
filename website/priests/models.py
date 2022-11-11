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


class Priest(models.Model):
    objects = models.Manager()      #Our default Manager
    published = PublishedManager()  #Our Custom Model Manager

    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published'),
    )
    status              =       models.CharField(max_length=10, choices=BLANK_CHOICE_DASH + list(STATUS_CHOICES))
    full_name           =       models.CharField(max_length=400)
    image_370_by_410    =       models.ImageField(blank=True, null=True)
    slug                    =       models.SlugField(max_length=200, blank=True, null=True)
    designation         =       models.CharField(max_length=200)
    snippet                    =       models.TextField(blank=True, null=True)
    speech                    =       models.TextField(blank=True, null=True)
    created             =       models.DateTimeField(auto_now_add=True)
    updated             =       models.DateTimeField(auto_now=True)

    class Meta:
    	verbose_name = 'Priest'
    	verbose_name_plural = 'Priests'

    def __str__(self):
    	return self.full_name

    def get_absolute_url(self):
        return reverse("priests:priest_details", args=[self.id, self.slug])



@receiver(pre_save, sender=Priest)
def pre_save_slug1(sender, **kwargs):
    slug = slugify(kwargs['instance'].full_name)
    kwargs['instance'].slug = slug

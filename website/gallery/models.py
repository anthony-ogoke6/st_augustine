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




class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status="published")





class Gallery(models.Model):
    objects = models.Manager()      #Our default Manager
    published = PublishedManager()  #Our Custom Model Manager

    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published'),
    )
    title               =       models.ForeignKey(Event, on_delete=models.CASCADE, related_name='occasion')
    image_400_400   =       models.ImageField(blank=True, null=True)
    video               =       models.FileField(blank=True, null=True)
    body                =       models.TextField(blank=True, null=True)
    created             =       models.DateTimeField(auto_now_add=True)
    updated             =       models.DateTimeField(auto_now=True)



    class Meta:
        ordering = ['-id']
        verbose_name = 'Gallery'
        verbose_name_plural = 'Gallery'

    def __str__(self):
        return self.title.title


    # def get_absolute_url(self):
    #     return reverse("gallery:gallery_detail", args=[self.id, self.slug])




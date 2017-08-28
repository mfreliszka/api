# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):

    # Fields

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    text = models.TextField(max_length=140)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    long = models.DecimalField(max_digits=9, decimal_places=6)

    # Relationship Fields
    #owner = models.ForeignKey(User, related_name='Posts', on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    
    def save(self, *args, **kwargs):
        
        super(Post, self).save(*args, **kwargs)


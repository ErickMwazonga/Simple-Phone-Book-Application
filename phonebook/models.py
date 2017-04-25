# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.db import models

# Create your models here.
class Contact(models.Model):
    '''
    A database representation of a PhoneBook
    '''
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.IntegerField(default=0, unique=True)
    email = models.EmailField()
    location = models.CharField(max_length=200)
    emergency_contact = models.IntegerField(default=0, unique=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.lastname)

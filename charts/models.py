# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class DataModel(models.Model):
    region = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=8, decimal_places=2)

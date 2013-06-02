from django.db import models
import pymongo
from liveinfo.utils import db, HTTPTools
from django.utils import timezone

# Create your models here.
def get_from_db(category):
    infodb =db.getConnection()
    cursor = infodb.info.find( { 'category' : category})
    out = []
    result = {}
    for infoItem in cursor:
        result = infoItem
        out.append(result)
    return out

class Doktor(models.Model):
	location = models.CharField(max_length=200)
	number = models.CharField(max_length=15)

	def __unicode__(self):  # Python 3: def __str__(self):
        	return self.location

class Wifi(models.Model):
	location = models.CharField(max_length=200)
        username = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	def __unicode__(self):  # Python 3: def __str__(self):
                return self.location
class Food(models.Model):

	location = models.CharField(max_length=200)
	number = models.CharField(max_length=15)

	def __unicode__(self):  # Python 3: def __str__(self):
                return self.location

class Siginak(models.Model):
	location = models.CharField(max_length=200)
        name = models.CharField(max_length=150)
	def __unicode__(self):  # Python 3: def __str__(self):
                return self.location


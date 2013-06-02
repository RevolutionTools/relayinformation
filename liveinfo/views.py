# Create youwwr views here.
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.mail import send_mail
import pymongo
from liveinfo.utils import db, HTTPTools
from liveinfo.models import Doktor, Wifi, Siginak, Food

def get_doktor_from_db(category):
    infodb =db.getConnection()
    cursor = infodb.info.find( { 'category' : category})
    out = []
    result = {}
    for infoItem in cursor:
        result = infoItem
	out.append(result)
    return out


def mainView(request):

	FoodList = Food.objects.all().order_by('location')
	doctorList = Doktor.objects.all().order_by('location')
	siginmaList = Siginak.objects.all().order_by('location')
	wifiList = Wifi.objects.all().order_by('location')

	result_dict = get_doktor_from_db('doktor')
	print "OUT dict is"	
	print result_dict
	context = {'output' : FoodList, 'doctorlist': doctorList, 'siginmalist' : siginmaList, 'wifilist': wifiList}
	return render_to_response('mainpage.html', context)

def indexView(request):

        result_dict = get_doktor_from_db('doktor')
        print "OUT dict is"
        print result_dict
        return render_to_response('index.html', result_dict)

from django.contrib import admin
from liveinfo.models import Doktor, Wifi, Food, Siginak
class PollAdmin(admin.ModelAdmin):
    fields = ['number', 'question']

admin.site.register(Doktor)
admin.site.register(Wifi)
admin.site.register(Food)
admin.site.register(Siginak)

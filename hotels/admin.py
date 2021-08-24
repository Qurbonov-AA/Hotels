from django.contrib import admin
from hotels.models import Hotels,Rooms,description_list,Guests  #add Services
from django import forms

admin.site.register(Hotels)
#admin.site.register(Services)
admin.site.register(Rooms)
admin.site.register(description_list)
admin.site.register(Guests)

from django.contrib import admin
from .models import Event, Exhibitor, Leads, Attendee
# Register your models here.

admin.site.register((Event, Exhibitor, Leads, Attendee))
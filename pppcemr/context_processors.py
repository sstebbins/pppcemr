from .models import *

def offices_processor(request):
    offices = Office.objects.all()
    return {'offices': offices}

def open_encounters_processor(request):
    open_encounters = Encounter.objects.filter(is_open = True)
    return {'open_encounters' : open_encounters}
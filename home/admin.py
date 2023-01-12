from django.contrib import admin
from .models import TourPackage

class TourPackageAdmin(admin.ModelAdmin):
    list_display = ("name","location","duration","img","discount","date","person","desc","price","rating")





admin.site.register(TourPackage , TourPackageAdmin)
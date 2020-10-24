from django.contrib import admin
from .models import Chemical, Commodity, ChemicalComposition

# Register your models here.

admin.site.register(Chemical)
admin.site.register(Commodity)
admin.site.register(ChemicalComposition)

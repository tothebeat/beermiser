from django.contrib import admin
from .models import Bar, Beer

class BeerAdmin(admin.ModelAdmin):
    list_filter = ['name', 'bar', 'price_usd']
    list_display = ('name', 'bar', 'fluid_ounces', 'price_usd', 'alcohol_by_volume', 'alcohol_fluid_ounces', 'alcohol_per_dollar')

admin.site.register(Bar)
admin.site.register(Beer, BeerAdmin)

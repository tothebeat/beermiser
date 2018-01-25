from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.shortcuts import render
from .models import Bar, Beer

def main(request):
    bars = Bar.objects.all()
    return render(request, 'bars/main.html', {'bars': bars})


class BarDetailView(DetailView):
    model = Bar


class BeerDetailView(DetailView):
    model = Beer


class BeerCreateView(CreateView):
    model = Beer
    fields = ['bar', 'name', 'fluid_ounces', 'price_usd', 'alcohol_by_volume']


class BarCreateView(CreateView):
    model = Bar
    fields = ['name', 'street_address', 'city', 'state']

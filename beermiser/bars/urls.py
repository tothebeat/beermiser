from django.urls import path
from .views import (
        main,
        BarCreateView,
        BeerCreateView,
        BarDetailView,
        BeerDetailView
        )
from . import views

urlpatterns = [
    path(r'', main, name='main'),
    path(r'add/bar/', BarCreateView.as_view(), name='add_bar'),
    path(r'add/beer/', BeerCreateView.as_view(), name='add_beer'),
    path(r'bar/<int:pk>/', BarDetailView.as_view(), name='bar_detail'),
    path(r'beer/<int:pk>/', BeerDetailView.as_view(), name='beer_detail'),
]

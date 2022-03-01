from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('edit/<id>',views.edit, name='edit'),
    path('search',views.search, name='search'),
    path('api/chart/data',views.ChartData, name='graph'),

]

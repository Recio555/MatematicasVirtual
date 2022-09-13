from django.urls import path
#from django.views.generic import TemplateViews
from Calculo_I import views as Calculo_I_views

urlpatterns = [
    path('', Calculo_I_views.index, name = 'index'),
    path('home', Calculo_I_views.home, name = 'home'),
]
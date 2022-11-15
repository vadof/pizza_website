from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('menu/pizza/', pizza_menu, name='pizza'),
    path('menu/burger/', burger_menu, name='burger'),
    path('menu/drinks/', drinks_menu, name='drinks'),
]

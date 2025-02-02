from django.urls import path
from .views import home, reference_list, cheatsheet_list

urlpatterns = [
    path('', home, name='home'),
    path('references/', reference_list, name='reference_list'),
    path('cheatsheets/lists/', cheatsheet_list, name='cheatsheet_list'),
]
from django.urls import path
from .views import home, reference_list, cheatsheet_list, submit_cheatsheet, cheatsheet_detail

urlpatterns = [
    path('', home, name='home'),
    path('references/', reference_list, name='reference_list'),
    path('cheatsheets/lists/', cheatsheet_list, name='cheatsheet_list'),
    path('cheatsheets/submit/', submit_cheatsheet, name='submit_cheatsheet'),
    path('cheatsheets/<int:cheatsheet_id>/', cheatsheet_detail, name='cheatsheet_detail'),
]
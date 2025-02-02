from django.shortcuts import render
from .models import Reference

def home(request):
    return render(request, 'refly/index.html')

def reference_list(request):
    references = Reference.objects.all()
    return render(request, 'refly/reference_list.html', {'references': references})

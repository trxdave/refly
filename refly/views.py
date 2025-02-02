from django.shortcuts import render
from .models import Reference, CheatSheet

def home(request):
    """
    Render the homepage.
    """
    return render(request, 'refly/index.html')

def reference_list(request):
    """
    Retrieve all references from the database and render them
    in the reference list template.
    """
    references = Reference.objects.all()
    return render(request, 'refly/reference_list.html', {'references': references})

def cheatsheet_list(request):
    cheatsheets = CheatSheet.objects.all()
    categories = CheatSheet.objects.values_list('category', flat=True).distinct()
    return render(request, 'cheatsheets/lists.html', {'cheatsheets': cheatsheets, 'categories': categories})

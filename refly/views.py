from django.shortcuts import render, get_object_or_404
from .models import Reference, CheatSheet

def home(request):
    """
    Homepage
    """
    cheatsheets = CheatSheet.objects.order_by('?')[:3]
    return render(request, 'refly/index.html', {'cheatsheet': cheatsheets})

def reference_list(request):
    """
    Retrieve all references from the database and render them
    in the reference list template.
    """
    references = Reference.objects.all()
    return render(request, 'refly/reference_list.html', {'references': references})

def cheatsheet_list(request):
    """Fetch and filter cheatsheets based on user search."""
    query = request.GET.get('q', '')  # Get search query
    if query:
        cheatsheets = CheatSheet.objects.filter(title__icontains=query) | CheatSheet.objects.filter(category__icontains=query)
    else:
        cheatsheets = CheatSheet.objects.all()
    
    categories = CheatSheet.objects.values_list('category', flat=True).distinct()
    
    return render(request, 'cheatsheets/lists.html', {
        'cheatsheets': cheatsheets,
        'categories': categories,
        'query': query
    })

def submit_cheatsheet(request):
    if request.method == "POST":
        form = CheatSheetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cheatsheet_list')  # Redirect to cheat sheets page
    else:
        form = CheatSheetForm()

    return render(request, 'cheatsheets/submit.html', {'form': form})


def cheatsheet_detail(request, cheatsheet_id):
    cheat = get_object_or_404(CheatSheet, id=cheatsheet_id)
    return render(request, 'cheatsheets/detail.html', {'cheat': cheat})
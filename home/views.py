from django.shortcuts import render

# Create your views here.
def get_index(request):
    """A view that displays the index page"""
    return render(request, "index.html")
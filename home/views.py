from django.shortcuts import render
from django.http import HttpResponse
from babysitters.choices import numbers_choices, minder_choices, county_choices

from babysitters.models import Babysitter

def get_index(request):
    babysitters = Babysitter.objects.order_by('-list_date').filter()[:3]

    context = {
        'babysitters': babysitters,
        'county_choices': county_choices,
        'minder_choices': minder_choices,
        'numbers_choices': numbers_choices
    }

    return render(request, 'index.html', context)
    
# Error Pages
def server_error(request):
    return render(request, 'errors/500.html')
 
def not_found(request):
    return render(request, 'errors/404.html')
 
def permission_denied(request):
    return render(request, 'errors/403.html')
 
def bad_request(request):
    return render(request, 'errors/400.html')
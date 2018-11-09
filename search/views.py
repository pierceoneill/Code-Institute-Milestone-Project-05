from django.shortcuts import render
from babysitters.models import Babysitter

# Create your views here.

def do_search(request):
    babysitters = Babysitter.objects.filter(firstName__icontains=request.GET['q'])
    return render(request, "babysitters.html", {"babysitters":babysitters})
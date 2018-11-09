from django.shortcuts import render, get_object_or_404
from .models import Babysitter


# Create your views here.
def all_babysitters(request):
    babysitters = Babysitter.objects.all()
    return render(request, "babysitters.html", {"babysitters": babysitters})

def babysitter_profile(request, id):
    """A view that displays the profile page of a registered babysitter"""
    babysitter = get_object_or_404(Babysitter, id=id)
    return render(request, "babysitter_profile.html", {'babysitter': babysitter}, )

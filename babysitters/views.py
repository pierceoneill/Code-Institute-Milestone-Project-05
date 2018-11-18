from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Babysitter, Education, Reference, Work

# Create your views here.
def all_babysitters(request):
    babysitters = Babysitter.objects.all()
    return render(request, "babysitters.html", {"babysitters": babysitters})
    
def babysitter_profile(request, id):
    """A view that displays the profile page of a registered babysitter"""
    babysitter = get_object_or_404(Babysitter, id=id)
    reference_qs = Reference.objects.filter(babysitter_id=babysitter.id)
    education_qs = Education.objects.filter(babysitter_id=babysitter.id)
    work_qs = Work.objects.filter(babysitter_id=babysitter.id)
    return render(request, "babysitter_profile.html", {
        'babysitter': babysitter,
        'education_qs': education_qs,
        'reference_qs': reference_qs,
        'work_qs': work_qs}
    )

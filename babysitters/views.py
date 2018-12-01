from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Babysitter, Education, Reference, Work
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import numbers_choices, minder_choices, county_choices


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


def index(request):
  babysitters = Babysitter.objects.order_by('-list_date').filter(is_published=True)

  paginator = Paginator(babysitters, 6)
  page = request.GET.get('page')
  paged_listings = paginator.get_page(page)

  context = {
    'babysitters': paged_listings
  }

  return render(request, 'babysitters.html', context)

def babysitter(request, babysitter_id):
  babysitter = get_object_or_404(Babysitter, pk=babysitter_id)

  context = {
    'babysitter': babysitter
  }

  return render(request, 'babysitter_profile.html', context)
    

def search(request):
  queryset_list = Babysitter.objects.order_by()

  # Keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(description__icontains=keywords)

  # City
  if 'city' in request.GET:
    city = request.GET['city']
    if city:
      queryset_list = queryset_list.filter(city__iexact=city)

  # State
  if 'state' in request.GET:
    state = request.GET['state']
    if state:
      queryset_list = queryset_list.filter(state__iexact=state)

  # Bedrooms
  if 'bedrooms' in request.GET:
    bedrooms = request.GET['bedrooms']
    if bedrooms:
      queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

  # Price
  if 'price' in request.GET:
    price = request.GET['price']
    if price:
      queryset_list = queryset_list.filter(price__lte=price)

  context = {
    'county_choices': county_choices,
    'minder_choices': minder_choices,
    'numbers_choices':numbers_choices,
    'babysitters': queryset_list,
    'values': request.GET
  }

  return render(request, 'search.html', context)
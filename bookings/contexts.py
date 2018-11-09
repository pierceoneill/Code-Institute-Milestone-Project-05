from django.shortcuts import get_object_or_404
from babysitters.models import Babysitter


def bookings_contents(request):
    """
    Ensures that the bookings contents are available when rendering every page
    """
    
    bookings = request.session.get('bookings', {})
    
    bookings_items = []
    total = 0
    babysitter_count = 0
    for id, quantity in bookings.items():
        babysitter = get_object_or_404(Babysitter, pk=id)
        total += quantity * babysitter.price
        babysitter_count += quantity
        bookings_items.append({'id':id, 'quantity': quantity, 'babysitter': babysitter})
        
    return { 'bookings_items': bookings_items, 'total': total, 'babysitter_count': babysitter_count }
    
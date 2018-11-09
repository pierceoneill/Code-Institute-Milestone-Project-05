from django.shortcuts import render, redirect, reverse

# Create your views here.

def view_bookings(request):
    """A view that renders the bookings contents page"""
    return render(request, "bookings.html")
    
    
def add_to_bookings(request, id):
    """Add a quantity of the specified product to the bookings"""
    quantity=int(request.POST.get('quantity'))
    
    bookings = request.session.get('bookings', {})
    bookings[id] = bookings.get(id, quantity)
    
    request.session['bookings'] = bookings
    return redirect(reverse('index'))
    
    
def adjust_bookings(request, id):
    """Adjust the quantity of the specified product to the specified amount"""
    quantity = int(request.POST.get('quantity'))
    bookings = request.session.get('bookings', {})
    
    if quantity > 0:
        bookings[id] = quantity
    else:
        bookings.pop(id)
        
    request.session['bookings'] = bookings
    return redirect(reverse('view_bookings'))
from django.contrib import messages, auth
from accounts.forms import UserRegistrationForm, UserLoginForm, FullUserDetailsForm, KidDetailsForm
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse, get_object_or_404
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from .models import KidProfile, UserProfile

@login_required(login_url='/accounts/login')
def profile(request):
    kids = KidProfile.objects.filter(parent=request.user)
    adults = UserProfile.objects.filter(user=request.user)
    return render(request, 'profile.html', {'kids': kids}, {'adults': adults})

def update_profile(request):
    form=FullUserDetailsForm(request.POST, request.FILES)
    if form.is_valid():
        request.user.first_name=form.cleaned_data['first_name']
        request.user.last_name=form.cleaned_data['last_name']
        request.user.email=form.cleaned_data['email']
        request.user.profile.address1=form.cleaned_data['address1']
        request.user.profile.address2=form.cleaned_data['address2']
        request.user.profile.postcode=form.cleaned_data['postcode']
        request.user.profile.phone=form.cleaned_data['phone']
        request.user.profile.dob=form.cleaned_data['dob']
        request.user.profile.gender=form.cleaned_data['gender']
        request.user.profile.facebook=form.cleaned_data['facebook']
        request.user.profile.twitter=form.cleaned_data['twitter']
        request.user.profile.instagram=form.cleaned_data['instagram']
        request.user.save()
        return redirect(reverse('profile'))
    else: 
        return redirect('profile')

def update_profile_kid(request, id):
    kid = get_object_or_404(KidProfile, pk=id)
    form=KidDetailsForm(request.POST, request.FILES)
    if form.is_valid():
        kid.name=form.cleaned_data['name']
        kid.dob=form.cleaned_data['dob']
        kid.gender=form.cleaned_data['gender']
        kid.needs=form.cleaned_data['needs']
        kid.save()
        return redirect(reverse('profile'))
    else: 
        return redirect('profile')
        
def create_profile_kid(request):
    form=KidDetailsForm(request.POST, request.FILES)
    if form.is_valid():
        kid=KidProfile()
        kid.name=form.cleaned_data['name']
        kid.dob=form.cleaned_data['dob']
        kid.gender=form.cleaned_data['gender']
        kid.needs=form.cleaned_data['needs']
        kid.parent=request.user
        kid.save()
        return redirect(reverse('profile'))
        
def delete_profile_kid(request, id):
    kid = get_object_or_404(KidProfile, pk=id)
    kid.delete()
    return redirect(reverse('profile'))



def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=request.POST.get('username_or_email'),
                                     password=request.POST.get('password'))

            if user is not None:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")

                if request.GET and request.GET['next'] !='':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('babysitters'))
            else:
                form.add_error(None, "Your username or password was not recognised")
    else:
        form = UserLoginForm()

    args = {'form': form, 'next': request.GET['next'] if request.GET and 'next' in request.GET else ''}
    args.update(csrf(request))
    return render(request, 'login.html', args)



def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            user = auth.authenticate(username=request.POST.get('username'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('profile'))

            else:
                messages.error(request, "unable to log you in at this time!")

    else:
        form = UserRegistrationForm()

    args = {'form': form}

    return render(request, 'profile.html', args)
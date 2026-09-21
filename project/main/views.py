from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Advertisement
from django.core.paginator import Paginator

def advertisements(request):
    ads = Advertisement.objects.all().order_by('-created_at')
    paginator = Paginator(ads, 2)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {
        'page': page
    }
    return render(request, 'main/advertisements.html', context)

def advertisement_detail(request, id):
    ad = get_object_or_404(Advertisement, id=id)
    context = {
        'ad': ad
    }
    return render(request, 'main/advertisement_detail.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('advertisements')
    return render(request, 'main/login.html')

def logout_view(request):
    logout(request)
    return redirect('advertisements')

@login_required(login_url='login')
def add_advertisement(request):
    if request.method == 'POST':
        ad = Advertisement()
        ad.title = request.POST['title']
        ad.description = request.POST['description']
        ad.price = request.POST['price']
        ad.image = request.FILES.get('image')
        ad.owner = request.user
        ad.save()
        return redirect('advertisements')
    return render(request, 'main/add_advertisement.html')

@login_required(login_url='login')
def edit_advertisement(request, id):
    ad = get_object_or_404(Advertisement, id=id)
    if ad.owner != request.user and not request.user.is_superuser:
        return redirect('advertisements')
    if request.method == 'POST':
        ad.title = request.POST['title']
        ad.description = request.POST['description']
        ad.price = request.POST['price']
        if request.FILES.get('image'):
            ad.image = request.FILES.get('image')
        ad.save()
        return redirect('advertisement_detail', id=ad.id)
    context = {
        'ad': ad
    }
    return render(request, 'main/edit_advertisement.html', context)

@login_required(login_url='login')
def delete_advertisement(request, id):
    ad = get_object_or_404(Advertisement, id=id)
    if ad.owner != request.user and not request.user.is_superuser:
        return redirect('advertisements')
    if request.method == 'POST':
        ad.delete()
        return redirect('advertisements')
    context = {
        'ad': ad
    }
    return render(request, 'main/delete_advertisement.html', context)



@login_required(login_url='login')
def favorite_advertisement(request, id):
    ad = get_object_or_404(Advertisement, id=id)
    if request.user in ad.favorites.all():
        ad.favorites.remove(request.user)
    else:
        ad.favorites.add(request.user)
    return redirect('advertisements')


@login_required(login_url='login')
def favorite_advertisements(request):
    ads = request.user.favorite_ads.all().order_by('-created_at')
    context = {
        'ads': ads
    }
    return render(request, 'main/favorites.html', context)
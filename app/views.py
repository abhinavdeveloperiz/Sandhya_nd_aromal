from django.shortcuts import render
from .models import Gallery, Sandhya, Aromal,Banner,Audio

# Create your views here.

def index(request):
    gallery = Gallery.objects.order_by('-id')
    sandhya = Sandhya.objects.first()
    aromal = Aromal.objects.first()
    banner = Banner.objects.first()
    audio = Audio.objects.first()
    context = {
        'gallery': gallery,
        'sandhya': sandhya,
        'aromal': aromal,
        'banner': banner,
        'audio': audio,
    }
    return render(request, 'index.html',context)
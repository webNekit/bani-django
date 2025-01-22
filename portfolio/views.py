from django.shortcuts import render
from .models import Gallery

# Create your views here.
def index(request):
    galleries = Gallery.objects.filter(is_active=True)
    context = {
        'galleries': galleries
    }
    return render(request, 'portfolio/index.html', context)
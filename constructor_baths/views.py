from django.shortcuts import render, get_object_or_404
from .models import Bath, BathGallery, BathLayout

# Create your views here.
def index(request):
    baths = Bath.objects.filter(is_active=True).order_by('-id')
    context = {
        'baths': baths,
        'detail_url': 'constructor_baths:detail',
    }
    return render(request, 'constructor_baths/index.html', context)

def detail(request, slug):
    bath = get_object_or_404(Bath, slug=slug, is_active=True)
    galleries = BathGallery.objects.filter(bath=bath.pk)
    layouts = BathLayout.objects.filter(bath=bath.pk)
    context = {
        'bath': bath,
        'galleries': galleries,
        'layouts': layouts,
        'product_name': bath.title,
        'meta_title': bath.title,
        'meta_description': bath.description_primary,
    }
    return render(request, 'constructor_baths/detail.html', context)
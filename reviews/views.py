from django.shortcuts import render
from .models import Reviews

# Create your views here.
def index(request):
    reviews = Reviews.objects.filter(is_active=True)
    return render(request, 'reviews/index.html', {'reviews': reviews})
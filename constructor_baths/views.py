from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'constructor_baths/index.html')

def detail(request):
    return render(request, 'constructor_baths/detail.html')
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('constructor-baths/', include('constructor_baths.urls', namespace='constructor_baths')),
    path('ready-baths/', include('ready_baths.urls', namespace='ready_baths')),
    path('portfolio/', include('portfolio.urls', namespace='portfolio')),
    path('reviews/', include('reviews.urls', namespace='reviews')),
    path('', include('main.urls', namespace='main')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
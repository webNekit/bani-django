from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('telegram_feedback/', views.telegram_feedback, name='telegram_feedback'),
    path('', views.index, name='index'),
]
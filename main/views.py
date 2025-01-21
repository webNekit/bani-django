import requests
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from ready_baths.models import Bath, BathGallery, BathLayout


# Create your views here.
def index(request):
    baths = Bath.objects.filter(is_active=True).order_by('-id')[:9]
    context = {
        'baths': baths,
        'detail_url': 'ready_baths:detail',
    }
    return render(request, 'main/index.html', context)


from django.http import HttpResponse

def telegram_feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        product_name = request.POST.get('product_name', None)

        # Формируем сообщение для бота
        message = f"Имя: {name}\nТелефон: {phone}"
        if product_name:
            message += f"\nПродукт: {product_name}"

        # Отправляем данные в Telegram
        telegram_url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
        params = {
            'chat_id': settings.TELEGRAM_CHAT_ID,
            'text': message
        }

        try:
            response = requests.post(telegram_url, params=params)
            response.raise_for_status()  # если ошибка, она будет поймана ниже
        except requests.exceptions.RequestException as e:
            return HttpResponse(f"Ошибка при отправке сообщения: {str(e)}", status=500)

        return HttpResponse("Ваша заявка отправлена!")

    return HttpResponse("Метод не поддерживается", status=405)



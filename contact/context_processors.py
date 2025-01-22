from .models import ContactInfo

def contact_info(request):
    contact = ContactInfo.objects.last()
    return {
        'contact_info': contact
    }
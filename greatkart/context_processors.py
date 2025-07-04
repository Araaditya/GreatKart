from django.conf import settings

def paypal_keys(request):
    return {
        'PAYPAL_CLIENT_ID': settings.PAYPAL_CLIENT_ID
    }

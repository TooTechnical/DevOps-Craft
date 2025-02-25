from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import stripe
from services.models import Service, Order

stripe.api_key = settings.STRIPE_SECRET_KEY

@csrf_exempt
def create_checkout_session(request, service_id):
    service = Service.objects.get(id=service_id)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': service.name,
                },
                'unit_amount': int(service.price * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri('/success/'),
        cancel_url=request.build_absolute_uri('/cancel/'),
    )
    return JsonResponse({'sessionId': session.id})

@csrf_exempt
def stripe_webhook(request):
    # Webhook handling code
    pass

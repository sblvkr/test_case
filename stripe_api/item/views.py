import stripe
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from item.models import Item
from stripe_api.settings import STRIPE_PK_KEY, STRIPE_SK_KEY

stripe.api_key = STRIPE_SK_KEY


def item_detail(request, pk: int):
    item = get_object_or_404(Item, pk=pk)

    return render(
        request,
        'item/item_detail.html',
        {
            'item': item,
            'STRIPE_PK_KEY': STRIPE_PK_KEY,
        }
    )


def checkout_session(request, pk: int):
    item = get_object_or_404(Item, pk=pk)
    price = str(item.price).split('.')
    # так цена хранится и передается в правильном виде
    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                    'description': item.description,
                },
                'unit_amount': ''.join(price),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:4242/success',
        cancel_url='http://localhost:4242/cancel',
    )

    return JsonResponse(session)

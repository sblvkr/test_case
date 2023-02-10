from django.shortcuts import render, get_object_or_404

from item.models import Item


def item_detail(request, pk: int):
    item = get_object_or_404(Item, pk=pk)

    return render(
        request,
        'item/item_detail.html',
        {
            'item': item,
        }
    )

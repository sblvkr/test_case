from django.contrib import admin

from item.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'description'
        'price',
    )
    search_fields = ('name',)
    empty_value_display = '-пусто-'

from django.urls import path

from item.views import checkout_session, item_detail

urlpatterns = [
    path('buy/<int:pk>/', checkout_session, name='buy'),
    path('item/<int:pk>/', item_detail, name='item_detail'),
]

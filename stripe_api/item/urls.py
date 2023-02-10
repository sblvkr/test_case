from django.urls import path

from item.views import item_detail

urlpatterns = [
    path('buy/<int:pk>', ),
    path('item/<int:pk>', item_detail),
]

from django.urls import path, include
from .views import LclassListAPIView, SclassListAPIView, ItemListAPIView, SetItemAPIView, ItemTabelListAPIView, ItemsetListAPIView

urlpatterns = [
    path('large_classes/', LclassListAPIView.as_view()),
    path('small_classes/', SclassListAPIView.as_view()),
    path('items/', ItemListAPIView.as_view()),
    path('set_items/', SetItemAPIView.as_view()),
    path('item_table/', ItemTabelListAPIView.as_view()),
    path('item_sets/', ItemsetListAPIView.as_view())
]

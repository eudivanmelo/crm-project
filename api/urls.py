from django.urls import path
from .views.category import CategoryListCreate_APIView, CategoryRetrieveUpdateDestroy_APIView
from .views.product import ProductListCreate_APIView, ProductRetrieveUpdateDestroy_APIView
from .views.stockitem import StockItemListCreate_APIView, StockItemRetrieveUpdateDestroy_APIView
from .views.register import RegisterView


urlpatterns = [
    path("register/", RegisterView.as_view(), name="api-register"),

    path('categories/', CategoryListCreate_APIView.as_view(), name='api-category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroy_APIView.as_view(), name='api-category-detail'),

    path('products/', ProductListCreate_APIView.as_view(), name='api-product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroy_APIView.as_view(), name='api-product-detail'),

    path('stockitems/', StockItemListCreate_APIView.as_view(), name='api-stockitem-list-create'),
    path('stockitems/<int:pk>/', StockItemRetrieveUpdateDestroy_APIView.as_view(), name='api-stockitem-detail'),
]

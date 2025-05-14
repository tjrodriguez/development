from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.decorators import action
from .product_views import ProductViewSet, CartItemViewSet, PaymentViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'cart-items', CartItemViewSet)
router.register(r'payments', PaymentViewSet, basename='payment')

urlpatterns = [
    path('', include(router.urls)),
    path('payments/process/', PaymentViewSet.as_view({
        'post': 'process_payment'
    }), name='payment-process'),
]   
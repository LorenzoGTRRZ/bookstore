from django.urls import path, include
from rest_framework.routers import SimpleRouter

from product.viewsets import CategoryViewSet, ProductViewSet

router = SimpleRouter()
router.register(r"category", CategoryViewSet, basename="category")
router.register(r"product", ProductViewSet, basename="product")

urlpatterns = [
    path("", include(router.urls)),
]

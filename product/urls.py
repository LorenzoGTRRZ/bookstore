from django.urls import path, include
from rest_framework.routers import SimpleRouter

from product.viewsets import CategoryViewSet, ProductViewSet

router = SimpleRouter()
router.register(r"category", CategoryViewSet, basename="categorys")
router.register(r"product", ProductViewSet, basename="products")

urlpatterns = [
    path("", include(router.urls)),
]

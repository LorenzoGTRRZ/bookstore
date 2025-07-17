from django.test import TestCase
from product.models import Product
from product.factories import ProductFactory, CategoryFactory


class TestProductModel(TestCase):
    def setUp(self) -> None:
        self.category = CategoryFactory(title="electronics")
        self.product = ProductFactory(
            title="smartphone",
            description="Latest model with advanced features",
            price=1200,
            active=True,
        )
        self.product.category.add(self.category)

    def test_product_creation(self):
        product = Product.objects.get(id=self.product.id)

        self.assertEqual(product.title, "smartphone")
        self.assertEqual(product.description, "Latest model with advanced features")
        self.assertEqual(product.price, 1200)
        self.assertTrue(product.active)

    def test_product_category(self):
        product = Product.objects.get(id=self.product.id)

        self.assertEqual(product.category.count(), 1)
        self.assertEqual(product.category.first().title, "electronics")

    def test_product_str(self):
        self.assertEqual(str(self.product), "smartphone")

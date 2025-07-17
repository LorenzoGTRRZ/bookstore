from django.test import TestCase
from product.factories import ProductFactory
from order.factories import OrderFactory


class OrderModelTest(TestCase):

    def setUp(self) -> None:
        self.product1 = ProductFactory.create()
        self.product2 = ProductFactory.create()
        self.order = OrderFactory.create(product=[self.product1, self.product2])
        self.order.save()

    def test_order_creation(self):
        order = self.order
        self.assertEqual(order.user.username, self.order.user.username)
        self.assertEqual(order.product.count(), 2)

    def test_order_products_association(self):
        order = self.order
        self.assertTrue(self.product1 in order.product.all())
        self.assertTrue(self.product2 in order.product.all())

    def test_order_str(self):
        self.assertEqual(
            str(self.order), f"Order {self.order.id} by {self.order.user.username}"
        )

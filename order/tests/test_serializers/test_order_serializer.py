from django.test import TestCase

from order.factories import OrderFactory, ProductFactory
from order.serializers import OrderSerializer


class TestOrderSerializer(TestCase):
    def setUp(self) -> None:
        self.product_1 = ProductFactory()
        self.product_2 = ProductFactory()

        self.order = OrderFactory(product=(self.product_1, self.product_2))
        self.order_serializer = OrderSerializer(self.order)

    def test_order_serializer(self):
        serializer_data = self.order_serializer.data
        sorted_products = sorted(serializer_data["product"], key=lambda x: x["title"])
        expected_products = sorted([self.product_1.title, self.product_2.title])

        self.assertEqual(sorted_products[0]["title"], expected_products[0])
        self.assertEqual(sorted_products[1]["title"], expected_products[1])

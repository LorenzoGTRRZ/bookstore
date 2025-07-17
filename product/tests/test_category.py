from django.test import TestCase
from product.models import Category
from product.factories import CategoryFactory


class TestCategoryModel(TestCase):
    def setUp(self) -> None:
        self.category = CategoryFactory(
            title="electronics",
            slug="electronics",
            description="All kinds of electronic products.",
        )

    def test_category_creation(self):
        category = Category.objects.get(id=self.category.id)
        self.assertEqual(category.title, "electronics")
        self.assertEqual(category.slug, "electronics")
        self.assertEqual(category.description, "All kinds of electronic products.")
        self.assertTrue(category.active)

    def test_category_str(self):
        self.assertEqual(str(self.category), "electronics")

    def test_category_slug_unique(self):
        with self.assertRaises(Exception):
            CategoryFactory(title="furniture", slug="electronics")

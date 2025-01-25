from django.test import TestCase

from store.models import Product


class ProductTest(TestCase):
    def test_product_slug_is_automatically_generated(self):
        self.product = Product.objects.create(
            name="Sneakers BlueMountain",
            price=10,
            stock=10,
            description="The sneakers is great.",
        )
        self.assertEqual(self.product.slug, "sneakers-bluemountain")


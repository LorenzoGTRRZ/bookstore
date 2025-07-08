import factory
from django.contrib.auth.models import User

from api.models import Product


class ProductFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("pystr")
    description = factory.Faker("pystr")
    price = factory.Faker("pyint")

    class Meta:
        model = Product


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker("pystr")
    email = factory.Faker("pystr")

    class Meta:
        model = User